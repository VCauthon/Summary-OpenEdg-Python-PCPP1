from dataclasses import dataclass
from typing import List
from random import sample
import tkinter as tk
from tkinter import messagebox


@dataclass
class button_created:
    number: int
    active = True
    widget: tk.Button = None
    width = 10
    height = 2


def get_lesser_active_number(curr_list: List[int], min_number: int = None) -> int:
    "Retrieves the smallest number in the list"

    # Checks if the current number is the lesser one    
    curr_number = curr_list.pop(0)
    if not min_number:  # First iteration
        min_number = curr_number
    elif curr_number < min_number:
        min_number = curr_number

    # Stops the iteration
    if not curr_list:
        return min_number
    else:
        return get_lesser_active_number(curr_list, min_number)


def button_clicked(event: tk.Event):

    global curr_lesser_number, buttons_displayed

    selected_button: button_created = next(
        butt for butt in buttons_displayed
        if butt.widget == event.widget)

    # Disable the button and detect the next one
    if selected_button.number == curr_lesser_number:

        selected_button.active = False
        selected_button.widget.config(state="disabled")

        # Stops the game if all buttons have been selected
        pending_buttons = [butt.number for butt in buttons_displayed if butt.active]
        if not pending_buttons:
            window.after_cancel(id_timer)
            messagebox.showinfo("Ended", "You have won the game!")
            window.destroy()
        else:
            curr_lesser_number = get_lesser_active_number(pending_buttons)


def update_timer():
    "Updates the timer every second"

    global id_timer, timer

    # Check if the timer has ended
    curr_time = int(timer.cget("text")) - 1
    game_lost(curr_time)

    # Update the timer if there is still some time left
    timer.config(text=curr_time)
    id_timer = window.after(1000, update_timer)


def game_lost(timer: int):
    if timer == 0:
        messagebox.showerror("You lose", "The counter has reached 0 before the end of the game")
        window.destroy()

# Windows creation
window = tk.Tk()
window.title("Clicker")
window.resizable(width=False, height=False)


# Creating all the buttons
buttons_displayed = [button_created(num) for num in sample(range(1, 999), k=25)]
for index, butt in enumerate(buttons_displayed):
    butt.widget = tk.Button(window, height=butt.height, width=butt.width, text=butt.number)
    butt.widget.bind("<Button-1>", button_clicked)
    butt.widget.grid(row=index % 5, column=index // 5)

curr_lesser_number = get_lesser_active_number(
        [butt.number for butt in buttons_displayed
         if butt.active])

# Adds the timer
concrete_time = 100
timer = tk.Label(window, text=concrete_time, font=("Arial", "15", "bold"))
timer.grid(row=5, column=2)


# Program starts
id_timer = window.after(1000, update_timer)
window.mainloop()