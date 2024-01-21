from dataclasses import dataclass

import tkinter as tk
from tkinter import messagebox

@dataclass
class OptionsField:
    entry: tk.Entry
    value: tk.StringVar


def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def calculate():

    entry_field_1 = OptionsField(
            entry=field_1,
            value=input_1,
        )
    entry_field_2 = OptionsField(
            entry=field_2,
            value=input_2,
        )

    entry_field_1.entry.config(background="white")
    entry_field_2.entry.config(background="white")

    print(operation.get())
    if is_float(entry_field_1.value.get()) and is_float(entry_field_2.value.get()):
            
            val1 = float(entry_field_1.value.get())
            val2 = float(entry_field_2.value.get())
            
            if operation.get()=="+":
                total = val1 + val2
            elif operation.get()=="-":
                total = val1 - val2
            elif operation.get()=="*":
                total = val1 * val2
            elif operation.get()=="/":
                total = val1 / val2
            messagebox.showinfo("Response",
                                f"Total\n{val1}{operation.get()}{val2}={total}")
    else:
        # The exercise says that focus should be used, however, setting a red border is better considering 
        # that both fields can be misinformed
        if not is_float(entry_field_1.value.get()) or not entry_field_1.value.get():
            entry_field_1.entry.config(background="red")
        if not is_float(entry_field_2.value.get()) or not entry_field_2.value.get():
            entry_field_2.entry.config(background="red")
        
        messagebox.showerror("Error", "There are invalid data into the fields")
        

window = tk.Tk()
window.title("Calculator")

# Observe variable
input_1 = tk.StringVar()
input_2 = tk.StringVar()

operation = tk.StringVar()
operation.set("+")


# Widget creation
field_1 = tk.Entry(window, textvariable=input_1)
field_2 = tk.Entry(window, textvariable=input_2)
radius_sum = tk.Radiobutton(window, text="+", variable=operation, value="+")
radius_min = tk.Radiobutton(window, text="-", variable=operation, value="-")
radius_mul = tk.Radiobutton(window, text="*", variable=operation, value="*")
radius_div = tk.Radiobutton(window, text="/", variable=operation, value="/")
but_eva = tk.Button(window, text="Evaluate", command=calculate)

# Placing widgets
field_1.grid(column=0, row=2)
radius_sum.grid(column=1, row=0)
radius_min.grid(column=1, row=1)
radius_mul.grid(column=1, row=2)
radius_div.grid(column=1, row=3)
but_eva.grid(column=1, row=4)
field_2.grid(column=2, row=2)

window.mainloop()