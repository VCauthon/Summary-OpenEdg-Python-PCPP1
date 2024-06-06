from dataclasses import dataclass, field
import csv
import os
from typing import List


@dataclass
class Results:
    exam: str
    id: str
    score: int
    grade: bool


@dataclass
class SubjectNotes:
    exam_name: str
    candidates: List[Results] = field(default_factory=list)
    total_candidates: int = 0
    total_passed: int = 0
    total_failed: int = 0
    best_score: int = 0
    worst_score: int = 100


class SummaryNotes:
    def __init__(self, path_notes: str) -> None:
        self.raw_results: List[Results] = self.__parse_subject_notes(path_notes)
        self.summary: List[SubjectNotes] = self.__create_summary(self.raw_results)

    @staticmethod
    def __parse_subject_notes(path_notes: str) -> List[Results]:
        results = []

        with open(path_notes, newline='') as file:
            data = csv.DictReader(file)
            for score in data:
                results.append(
                    Results(
                        exam=score.get('Exam Name'),
                        id=score.get('Candidate ID'),
                        score=int(score.get('Score')),
                        grade=True if score.get('Grade')=='Pass' else False
                    )
                )

        return results

    def __create_summary(self, raw_results: List[Results]) -> None:
        summary = self.__splitting_results_by_subject(raw_results)

        # Getting each result by score
        for subject in summary:
            subject.total_candidates = len(subject.candidates)
            for candidate in subject.candidates:

                if candidate.score == 33:
                    print("hi")

                if candidate.grade:
                    subject.total_passed += 1
                else:
                    subject.total_failed += 1

                subject.best_score = candidate.score if candidate.score > subject.best_score else subject.best_score
                subject.worst_score = candidate.score if candidate.score < subject.worst_score else subject.worst_score

        return summary

    @staticmethod
    def __splitting_results_by_subject(raw_results: List[Results]) -> List[SubjectNotes]:
        summary: List[SubjectNotes] = []

        # Splitting results by subject
        for result in raw_results:

            # Adds the result into its group
            if concrete_subject := next((det for det in summary if det.exam_name == result.exam), None):

                # Only unique candidates will be added
                if not next((can for can in concrete_subject.candidates if can.id==result.id), None):
                    concrete_subject.candidates.append(result)

            # Create a new group because it doesn't belong into any existing one
            else:
                summary.append(
                    SubjectNotes(
                        exam_name=result.exam,
                        candidates=[result]))

        return summary

    def save_summary(self, path: str) -> None:
        with open(path, '+w', newline='') as file:
            new_csv = csv.DictWriter(file, fieldnames=['Exam Name', 'Number of Candidates', 'Number of Passed Exams', 'Number of Failed Exams', 'Best Score', 'Worst Score'])

            new_csv.writeheader()
            for subject in self.summary:
                new_csv.writerow({
                    'Exam Name': subject.exam_name,
                    'Number of Candidates': subject.total_candidates,
                    'Number of Passed Exams': subject.total_passed,
                    'Number of Failed Exams': subject.total_failed,
                    'Best Score': subject.best_score,
                    'Worst Score': subject.worst_score
                })

if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))

    summary_results = SummaryNotes('../persistance/exam_results.csv')
    summary_results.save_summary('../persistance/exam_results_summary.csv')
