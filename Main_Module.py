import tkinter as tk
from tkinter import ttk

title = "Main Module"


def open_dice_module():
    import Dice_Module

    Dice_Module.root.mainloop()


root = tk.Tk()
root.title(title)
root.geometry("510x1000")
button_open_dice = tk.Button(
    root,
    text="Open Dice Roller",
    command=open_dice_module,
    bg="blue",
    fg="white",
    font=("Arial", 14, "bold"),
)


def open_test_module():
    import Test_Module

    Test_Module.main()


button_open_test = tk.Button(
    root,
    text="Open Test Module",
    command=open_test_module,
    bg="green",
    fg="white",
    font=("Arial", 14, "bold"),
)
button_open_dice.pack(pady=50)
button_open_test.pack(pady=50)


def open_files_module():
    import Files_Module

    Files_Module.root.mainloop()


button_open_files = tk.Button(
    root,
    text="Open Files Module",
    command=open_files_module,
    bg="purple",
    fg="white",
    font=("Arial", 14, "bold"),
)
button_open_files.pack(pady=50)


def open_color_module():
    import Color_Module

    Color_Module.root.mainloop()


button_open_color = tk.Button(
    root,
    text="Open Color Module",
    command=open_color_module,
    bg="orange",
    fg="white",
    font=("Arial", 14, "bold"),
)


def open_dot_module():
    import Dot_Module

    Dot_Module.root.mainloop()


button_open_dot = tk.Button(
    root,
    text="Open Dot Module",
    command=open_dot_module,
    bg="cyan",
    fg="black",
    font=("Arial", 14, "bold"),
)


def open_scanner_module():
    import Scanner_Module

    Scanner_Module.root.mainloop()


button_open_scanner = tk.Button(
    root,
    text="Open Scanner Module",
    command=open_scanner_module,
    bg="red",
    fg="white",
    font=("Arial", 14, "bold"),
)


button_open_scanner.pack(pady=50)

button_open_dot.pack(pady=50)
button_open_color.pack(pady=50)


def open_notepad_module():
    import Notepad_Module

    Notepad_Module.root.mainloop()


button_open_notepad = tk.Button(
    root,
    text="Open Notepad Module",
    command=open_notepad_module,
    bg="brown",
    fg="white",
    font=("Arial", 14, "bold"),
)
button_open_notepad.pack(pady=50)
root.mainloop()
