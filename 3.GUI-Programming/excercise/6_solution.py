from typing import List, Callable, Tuple
import re
import tkinter as tk


numbers: List[str] = [""]
curr_position = 0


def refresh_screen(clean_variables_after_clean: bool = False) -> Callable:    
    def func_wrapper(func):
        def args_wrapper(*args, **kwargs):

            # Executes the wrapped function
            func(*args, **kwargs)

            # Update the screen with the user inputs
            data_shown = ""
            for position, val in enumerate(numbers, 1):
                data_shown += val

                # Don't add a last space of its the last iteration
                if position != len(numbers):
                    data_shown += " "

            screen_zone.set(data_shown)
            if clean_variables_after_clean:
                _clean_variables_saved()

        return args_wrapper
    return func_wrapper


# Function to update number
@refresh_screen()
def update_number(event: tk.Event) -> None:
    global numbers, curr_position

    select_option = event.widget.cget("text")

    # Clean the screen
    if select_option == "C":
        _clean_variables_saved()

    # Update the actual number
    else:
        # Constrains before update
        if _invalid_first_values(select_option) and _no_more_points(select_option) and _no_more_zero(select_option):
            numbers[curr_position] += event.widget.cget("text")


def _no_more_zero(val: str):
    return not (numbers[curr_position] == "0" and (val == "0"))


def _no_more_points(val: str):
    return not (numbers[curr_position].count(".") == 1 and val == ".")


def _invalid_first_values(val: str):
    return not (numbers[curr_position] == "" and (val == "."))


def _clean_variables_saved() -> None:
    global numbers, curr_position
    numbers = [""]
    curr_position = 0


@refresh_screen()
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


@refresh_screen(True)
def operate_results(_: tk.Event) -> None:
    global numbers

    # At least has all numbers needed to make an operation
    if len(numbers)>2:

        try:

            # Expected order to operate
            for sign in ["*", "/", "+", "-"]:

                # Do it until there are no more signs in the operation
                while sign in numbers:
                    if position := numbers.index(sign):
                        results = _make_the_operation(*_get_nums_an_signs(position))

                        # Restructure the list with the results of the operation
                        if len(numbers) == 3:
                            numbers = [str(results)]
                        else:
                            numbers[position+1] = results
                            numbers.pop(position), numbers.pop(position-1)

        except Exception:
            numbers=["Error!"]


def _get_nums_an_signs(position: int) -> Tuple[int, str, int]:
    return float(numbers[position-1]), numbers[position], float(numbers[position+1])


def _make_the_operation(num1: int, sign: str, num2: int) -> float:
    if sign == "+":
        return num1 + num2
    elif sign == "-":
        return num1 - num2
    elif sign == "*":
        return num1 * num2
    elif sign == "/":
        return num1 / num2


@refresh_screen()
def invert_curr_val(event: tk.Event) -> None:
    global numbers

    if numbers[curr_position]:

        # Add or remove the sign at the start
        if "-" in numbers[curr_position]:
            numbers[curr_position] = numbers[curr_position][1:]
        else:
            numbers[curr_position] = "-" + numbers[curr_position]


def _curr_position_has_data() -> bool:
    return len(numbers[curr_position]) != 0


def _curr_position_is_number() -> bool:
    return _is_float(numbers[curr_position]) or numbers[curr_position].isnumeric


def _is_float(num: str) -> bool:
    pattern = r"^-?\d+\.\d+$"
    return re.match(pattern, num) is not None


# Functions to create the screen
def add_pad_number(widget: tk.Widget, pad_nums: List[str], callback: Callable) -> None:
    pad_nums = [pad_nums[v : v + 3] for v in range(0, len(pad_nums), 3)][::-1]
    last_nums = [".", "C", "0"]
    for row, pad_num in enumerate(pad_nums + [last_nums], 1):
        for col, num in enumerate(pad_num):
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
add_mutators(wnd, ("=", operate_results), ("+/-", invert_curr_val))
add_signs(wnd, save_sign)

# Start the GUI
wnd.mainloop()
