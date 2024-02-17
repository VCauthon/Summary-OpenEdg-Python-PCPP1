from dataclasses import dataclass
from typing import List
import tkinter as tk
from tkinter import messagebox
from random import randrange
import sys


class Owner:
    User="user"
    Computer="computer"


class PositionActions:
    def move_computer(self):
        self.widget.config(text="X", fg="red")
        self.set = Owner.Computer

    def move_user(self):
        self.widget.config(text="O", fg="green")
        self.set = Owner.User


@dataclass
class Position(PositionActions):
    widget: tk.Button
    set: Owner = None


def clicking_button(event: tk.Event) -> None:
    # Makes user and computer movement and checks if the game has ended
    sel_button = _get_button_poss(event.widget)

    # The selected button is empty
    if sel_button.set is None:

        # User movements
        sel_button.move_user()
        _check_game_ended_by(Owner.User)

        # Computer movements
        _decide_computer_movement().move_computer()
        _check_game_ended_by(Owner.Computer)


def _get_button_poss(widget: tk.Widget) -> Position:
    return next((
        row_b for col_b in list_buttons
        for row_b in col_b
        if row_b.widget == widget), None)


def _decide_computer_movement() -> Position:
    empty_positions = [row_b for col_b in list_buttons for row_b in col_b if row_b.set is None]
    return empty_positions[randrange(0, len(empty_positions))]


def _check_game_ended_by(player) -> None:
    table = _get_moves_from(player)

    if _check_diagonal_win(table):
        _end_game(player)

    # Check for lineal movements that wins the game
    for diagonal_check in range(3):
        h_win = _check_lineal_win(table[diagonal_check])
        v_win = _check_lineal_win([col[diagonal_check] for col in table])

        if h_win or v_win:
            _end_game(player)


def _get_moves_from(player: int) -> List[List[bool]]:
    return [[True if row_p.set==player else False for row_p in col_p] for col_p in list_buttons]


def _check_lineal_win(moves_made: List[bool]) -> bool:
    return len([mm for mm in moves_made if mm]) == 3


def _check_diagonal_win(table: List[List[bool]]) -> bool:

    # Check the first diagonal
    if all([table[val][val] for val in range(3)]):
        return True

    # Check the second diagonal
    if all([table[val][-(val+1)] for val in range(3)]):
        return True

    return False


def _end_game(player: str):
    messagebox.showinfo("Game ended", f"The {player} has won the game")
    wnd.after(100, sys.exit)


# Window creation
wnd = tk.Tk()
wnd.title("TicTacToe")

# Adding buttons
list_buttons: List[List[Position]] = []
for column in range(3):
    column_created: List[Position] = []
    
    # Creates the buttons and place it into the GUI
    for row in range(3):
        column_created.append(Position(tk.Button(wnd, height=10, width=20)))
        column_created[row].widget.bind("<Button-1>", clicking_button)
        column_created[row].widget.grid(row=row, column=column)

    # Place the row of buttons into the column
    list_buttons.append(column_created)

list_buttons[1][1].move_computer()
wnd.mainloop()