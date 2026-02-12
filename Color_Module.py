import tkinter as tk
from tkinter import colorchooser

title = "Color Module"


def color_pick_button():
    color_code = colorchooser.askcolor(title="Choose a color")
    if color_code[1] is not None:
        color_label.config(text=f"Selected Color: {color_code[1]}", bg=color_code[1])


root = tk.Tk()
root.title(title)
root.geometry("400x200")
color_button = tk.Button(
    root,
    text="Pick a Color",
    command=color_pick_button,
    bg="orange",
    fg="white",
    font=("Arial", 14, "bold"),
)
color_button.pack(pady=20)
color_label = tk.Label(root, text="Selected Color: None", font=("Arial", 14))
color_label.pack(pady=20)
root.mainloop()
