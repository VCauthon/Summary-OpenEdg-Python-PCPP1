from dataclasses import dataclass
import sqlite3
from typing import List, Dict, Callable


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


def display_needed_options(params: Dict[str, Callable[..., None]]):
    # Ask to the user the expected arguments to execute this function

    def func(func):
        def wrapper(*args, **kwargs):

            arguments = {}
            for param, rec_type in params.items():
                arguments[param] = rec_type(input(f"{param}="))

            return func(*args, **kwargs, **arguments)

        return wrapper
    return func



class TODO:

    def __init__(self) -> None:
        self.session = sqlite3.connect(':memory:')
        self.cursor = self.session.cursor()
        self.__set_table()

    @autocommit
    def __set_table(self):
        self.cursor.execute(
            'CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, name TEXT NOT NULL, priority INTEGER NOT NULL);')

    def show_tasks(self) -> List[Task]:
        results = self.cursor.execute('SELECT id, name, priority FROM tasks;')
        print([Task(*task) for task in results.fetchall()])

    @display_needed_options({"todo": str, "priority": int})
    @autocommit
    def add_task(self, todo: str, priority: int) -> None:
        if not todo or not priority:
            print("The method that creates function hasn't received all the expected arguments")
            return False
        else:
            # Updates the priority when task already exist
            if id := self.__find_task_by_name(todo):
                self.cursor.execute(f'UPDATE tasks SET priority = {priority} WHERE id = {id[0].id}')
            # Inserts a new task
            else:
                self.cursor.execute('INSERT INTO tasks (name, priority) VALUES (?, ?)', (todo, priority))
            return True

    def __find_task_by_name(self, todo: str) -> Task:
        results = self.cursor.execute('SELECT id, name, priority FROM tasks WHERE name = ?', (todo,))
        return [Task(*task) for task in results.fetchall()]

    def __find_task_by_id(self, id: int) -> Task:
        results = self.cursor.execute('SELECT id, name, priority FROM tasks WHERE id = ?', (id,))
        return next((Task(*task) for task in results.fetchall()), None)

    @display_needed_options({"id": int, "priority": int})
    @autocommit
    def change_priority(self, id: int, priority: int) -> None:
        if task := self.__find_task_by_id(id):
            if task.priority == priority:
                print("This task already has that priority!")
                print(f"TASK WITH ID ({id}): {task}")
            else:
                self.cursor.execute('UPDATE tasks SET priority=? WHERE id = ?', (priority, id))
        else:
            print(f"There are no task with this ID ({id})")

    @display_needed_options({"id": int})
    @autocommit
    def delete_task(self, id: int) -> None:
        if self.__find_task_by_id(id):
            self.cursor.execute('DELETE FROM tasks WHERE id = ?', (id,))
        else:
            print(f"There are no task with this ID ({id})")


def create_selector(inst: TODO) -> Dict[str, Callable[..., None]]:
    options = {f'{num+1}. {opt.replace("_", " ").capitalize()}': getattr(inst, opt)
            for num, opt in enumerate([sel for sel in dir(TODO) if not sel.startswith("_")])}
    options[f"{len(options)+1}. Exit"] = exit
    return options


if __name__ == "__main__":

    option_selector = create_selector(TODO())

    while True:
        print("".center(50, "*"))
        for tittle in option_selector.keys():
            print(tittle)

        try:
            selection = int(input("Chose one of the options shown".center(50, "*") + "\n>>> "))
        except ValueError:
            print("ERROR: The input inserted isn't a number")
            continue

        if sel := next((func for tittle, func in option_selector.items() if tittle.startswith(str(selection))), None):
            sel()
        else:
            print("ERROR: The inserted value doesn't exist in the list of option")
