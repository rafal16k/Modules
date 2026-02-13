import tkinter as tk
from tkinter import filedialog
import os

try:
    from PIL import Image, ImageTk

    PIL_AVAILABLE = True
except Exception:
    PIL_AVAILABLE = False

selected_file_label = None
file_icon_label = None


def file_path():
    global selected_file_label, file_icon_label
    filepath = filedialog.askopenfilename()

    if filepath:
        selected_file_label.config(text=f"Plik: {filepath}")

        if not PIL_AVAILABLE:
            file_icon_label.config(text="Pillow not installed", image="")
            return

        try:
            icon = Image.open(filepath)
            icon.thumbnail((100, 100))
            photo = ImageTk.PhotoImage(icon)
            file_icon_label.config(image=photo, text="")
            file_icon_label.image = photo
        except Exception:
            file_icon_label.config(text="Error", image="")


root = tk.Tk()
root.title("Files Module")
root.geometry("400x500")

tk.Button(
    root,
    text="Select File",
    bg="purple",
    fg="white",
    font=("Arial", 14, "bold"),
    command=file_path,
).pack(pady=20)

selected_file_label = tk.Label(
    root, text="Wybierz plik...", font=("Arial", 12), wraplength=350
)
selected_file_label.pack(pady=20)

file_icon_label = tk.Label(root, text="", bg="lightgray", width=150, height=100)
file_icon_label.pack(pady=20)

root.mainloop()
