from dataclasses import dataclass
import sqlite3
from typing import List, Tuple


@dataclass
class Task:
    id: int
    name: str
    priority: int

def autocommit(func):
    # Commits anything that the function has sent to the DB
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        instance: TODO = args[0]
        instance.session.commit()
        return result
    return wrapper


class TODO:

    def __init__(self) -> None:
        self.session = sqlite3.connect(':memory:')
        self.cursor = self.session.cursor()
        self.__set_table()

    @autocommit
    def __set_table(self):
        self.cursor.execute(
            'CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, name TEXT NOT NULL, priority INTEGER NOT NULL);')

    @autocommit
    def enter_task(self, todo: str, priority: int) -> None:
        if not todo or not priority:
            print("The method that creates function hasn't received all the expected arguments")
            return False
        else:
            # Updates the priority when task already exist
            if id := self.find_task(todo):
                self.cursor.execute(f'UPDATE tasks SET priority = {priority} WHERE id = {id[0].id}')
            # Inserts a new task
            else:
                self.cursor.execute('INSERT INTO tasks (name, priority) VALUES (?, ?)', (todo, priority))
            return True

    def find_task(self, todo: str) -> Task:
        results = self.cursor.execute(f'SELECT id, name, priority FROM tasks WHERE name = "{todo}";')
        return [Task(*task) for task in results.fetchall()]

    def show_task(self) -> List[Task]:
        results = self.cursor.execute('SELECT id, name, priority FROM tasks;')
        return [Task(*task) for task in results.fetchall()]


task_added = [
    ("My first task", 1),
    ("My second task", 2),
    ("My first task", 0),
    ("", 1),
    ("My first task", 3)
]

task_manager = TODO()

for task in task_added:
    if task_manager.enter_task(*task):
        print(task_manager.show_task())
