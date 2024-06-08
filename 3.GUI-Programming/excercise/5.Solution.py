import tkinter as tk


window = tk.Tk()

# Widget creation
label = tk.Label(window, text="Little label:")
background = tk.Frame(window, bg="blue", height=30, width=100)
button = tk.Button(text="Button")

value_checkbox = tk.IntVar()
value_checkbox.set(1)
check_button = tk.Checkbutton(window, text="Check Button", variable=value_checkbox)

textbox = tk.Entry(window, width=30)

value_radio = tk.StringVar()
value_radio.set("Salad")
radios_button_1 = tk.Radiobutton(window, text="Steak", variable=value_radio, value="Steak")
radios_button_2 = tk.Radiobutton(window, text="Salad", variable=value_radio, value="Salad")

label.pack()
background.pack()
button.pack(fill=tk.X)
check_button.pack()
textbox.pack()
radios_button_1.pack()
radios_button_2.pack()

window.mainloop()