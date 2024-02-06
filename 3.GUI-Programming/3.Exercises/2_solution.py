import tkinter as tk


POSITIONS = [(0, 0), (0, 200), (0, 400), (225, 0), (225, 200), (225, 400), (475, 0), (475, 200), (475, 400)]
CURR_POSITION = 0

def place(event: tk.Event):
    "Change the current position from the widget"

    global CURR_POSITION, catch_button
    CURR_POSITION += 1
    new_position = POSITIONS[CURR_POSITION % len(POSITIONS)]
    catch_button.place(y=new_position[0], x=new_position[1])


# Windows creation
window = tk.Tk()
window.title("Catch me!")
window.config(width=500, height=500)
window.resizable(width=False, height=False)

# Button added
catch_button = tk.Button(window, text="Catch me!")
catch_button.place(y=POSITIONS[CURR_POSITION][0], x=POSITIONS[CURR_POSITION][1])

# Change button placement logic
catch_button.bind("<Enter>", place)

# Program starts
window.mainloop()
