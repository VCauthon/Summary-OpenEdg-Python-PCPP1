from typing import Tuple, List
from tkinter import Tk, Button, Canvas


PHASES = (
    (True, False, False),
    (True, True, False),
    (False, False, True),
    (False, True, False),
)
current_position = 0

# Write your code here


def switch_next_lights() -> None:
    _update_lights(PHASES[_update_position(+1)])


def switch_previous_lights() -> None:
    _update_lights(PHASES[_update_position(-1)])


def _update_position(act: int) -> int:
    global current_position
    current_position = current_position + act
    return current_position % len(PHASES)


def _update_lights(state: Tuple[bool, bool, bool]) -> None:
    lights: List[Tuple[Canvas, str]] = [
        (light_1, "red"),
        (light_2, "yellow"),
        (light_3, "green"),
    ]
    for index, curr in enumerate(state):
        if curr:
            _set_light(*lights[index])  # Sends the light and its color
        else:
            _set_light(lights[index][0])  # Only sends its light


def _set_light(canvas: Canvas, color: str = "grey"):
    canvas.create_oval(10, 10, 170, 170, outline="black", fill=color, width=5)


# Window creation
window = Tk()
window.title("British lights")
window.resizable(False, False)

# Creating the canvas
base_lights = Canvas(window, background="#5e5e5e", width=200, height=500)
light_1 = Canvas(window, background="#5e5e5e", width=175, height=175)
_set_light(light_1)
light_2 = Canvas(window, background="#5e5e5e", width=175, height=175)
_set_light(light_2)
light_3 = Canvas(window, background="#5e5e5e", width=175, height=175)
_set_light(light_3)
light_1.pack()
light_2.pack()
light_3.pack()

# Adding its buttons
next_button = Button(window, text="Next", command=switch_next_lights)
previous_button = Button(window, text="Previous", command=switch_previous_lights)
exit_button = Button(window, text="Quit", command=window.destroy)
next_button.pack()
previous_button.pack()
exit_button.pack()

# Starts the lights
_update_lights(PHASES[current_position])

# The window starts
window.mainloop()
