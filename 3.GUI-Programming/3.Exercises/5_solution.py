from dataclasses import dataclass
from typing import List
import tkinter as tk
from tkinter import messagebox
from random import randrange


class Owner:
    User=0
    Computer=1


class PositionActions:
    def move_computer(self):
        self.Widget.config(text="X", fg="red")
        self.Set = Owner.Computer

    def move_user(self):
        self.Widget.config(text="O", fg="green")
        self.Set = Owner.User


@dataclass
class Position(PositionActions):
    Widget: tk.Button
    Set: Owner = None

# Window creation
wnd = tk.Tk()
wnd.title("TicTacToe")

# Adding buttons
list_buttons: List[Position] = []  # TODO: Use a matrix instead of a raw list
for bt_position in range(9):
    list_buttons.append(Position(tk.Button(wnd, height=10, width=20)))
    list_buttons[-1].Widget.grid(row=bt_position % 3, column=bt_position // 3)

list_buttons[4].move_computer()
wnd.mainloop()