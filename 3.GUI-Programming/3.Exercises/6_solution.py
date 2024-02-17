from typing import List, Callable
import re
import tkinter as tk


# Variables needed
numbers: List[str] = [""]
curr_position = 0


# Function to update number
def update_number(event: tk.Event) -> None:
    global numbers, curr_position

    select_option = event.widget.cget("text")

    # Clean the screen
    if select_option == "C":
        numbers = [""]
        curr_position = 0

    # Update the actual number
    else:
        # Constrains before update
        if _invalid_first_values(select_option) and _no_more_points(select_option):
            numbers[curr_position] += event.widget.cget("text")
    _refresh_screen()


def save_sign(event: tk.Event) -> None:
    global curr_position, numbers

    select_sign = event.widget.cget("text")

    # Saves the sign selected
    if _curr_position_is_number() and _curr_position_has_data():
        numbers.append(select_sign)
        numbers.append("")
        curr_position += 2

    # Updates the current sign
    elif len(numbers) != 1:
        numbers[curr_position - 1] = select_sign

    _refresh_screen()


def operate_results(event: tk.Event) -> None:
    pass


def invert_curr_val(event: tk.Event) -> None:
    pass


def _curr_position_is_number() -> bool:
    return _is_float(numbers[curr_position]) or numbers[curr_position].isnumeric


def _curr_position_has_data() -> bool:
    return len(numbers[curr_position]) != 0


def _refresh_screen() -> None:
    # Update the screen with the user inputs
    data_shown = ""
    for position, val in enumerate(numbers, 1):
        data_shown += val

        # Don't add a last space of its the last iteration
        if position != len(numbers):
            data_shown += " "

    screen_zone.set(data_shown)


def _is_float(num: str) -> bool:
    pattern = r"^-?\d+\.\d+$"
    return re.match(pattern, num) is not None


def _invalid_first_values(val: str):
    return not (numbers[curr_position] == "" and (val == "0" or val == "."))


def _no_more_points(val: str):
    return not (numbers[curr_position].count(".") == 1 and val == ".")


def add_pad_number(widget: tk.Widget, pad_nums: List[str], callback: Callable) -> None:
    pad_nums = [pad_nums[v : v + 3] for v in range(0, len(pad_nums), 3)]
    last_nums = [".", "C", "0"]
    for row, pad_num in enumerate(pad_nums + [last_nums], 1):
        for col, num in enumerate(pad_num[::-1]):
            button = tk.Button(widget, text=str(num))
            button.grid(column=col, row=row)
            button.bind("<Button-1>", callback)


def add_mutators(widget: tk.Widget, *args) -> None:
    for row, sign in enumerate(args, 3):
        button = tk.Button(widget, text=sign[0], width=2)
        button.grid(column=3, row=row)
        button.bind("<Button-1>", sign[1])


def add_signs(widget: tk.Widget, callback: Callable) -> None:
    for row, sign in enumerate(["+", "-", "*", "/"], 1):
        button = tk.Button(widget, text=sign)
        button.grid(column=4, row=row)
        button.bind("<Button-1>", callback)


# Creation of the window
wnd = tk.Tk()
wnd.title("Calculator")
wnd.resizable(False, False)

# Add numbers screen
screen_zone = tk.StringVar()
screen = tk.Label(
    wnd, bg="#ededed", width=28, borderwidth=1, textvariable=screen_zone, anchor="e"
)
screen.grid(column=0, row=0, columnspan=5)

# Add all the calculator
add_pad_number(wnd, [num for num in range(1, 10)], update_number)
# TODO: Pending to implement operate_results and invert_curr_val !!!
add_mutators(wnd, ("=", operate_results), ("+/-", invert_curr_val))
add_signs(wnd, save_sign)

# Start the GUI
wnd.mainloop()
