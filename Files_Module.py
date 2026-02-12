import tkinter as tk
from tkinter import filedialog
from PIL import Image, Image
import os

selected_file_label = None
file_icon_label = None


def file_path():
    global selected_file_label, file_icon_label
    file = filedialog.askopenfilename()

    if file:
        # Wyświetl ścieżkę
        selected_file_label.config(text=f"Plik: {file}")

        # Wyświetl ikonę
        try:
            icon = Image.open(file)
            icon.thumbnail((100, 100))
            photo = ImageTk.PhotoImage(icon)
            file_icon_label.config(image=photo)
            file_icon_label.image = photo
        except:
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
