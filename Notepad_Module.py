import math
import tkinter as tk
from tkinter import filedialog, messagebox
def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        try:
            with open(file_path, 'r') as file:
                content = file.read()
                text_area.delete(1.0, tk.END)
                text_area.insert(tk.END, content)
        except Exception as e:
            messagebox.showerror("Error", f"Could not open file: {e}")
def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        try:
            with open(file_path, 'w') as file:
                content = text_area.get(1.0, tk.END)
                file.write(content)
        except Exception as e:
            messagebox.showerror("Error", f"Could not save file: {e}")

root = tk.Tk()
root.title("Notepad Module")
root.geometry("1000x600")
text_area = tk.Text(root, wrap=tk.WORD, font=("Arial", 12))
text_area.pack(expand=True, fill=tk.BOTH)
button_frame = tk.Frame(root)
button_frame.pack(fill=tk.X)
open_button = tk.Button(button_frame, text="Open", command=open_file)
open_button.pack(side=tk.LEFT, padx=5, pady=5)
save_button = tk.Button(button_frame, text="Save", command=save_file)
save_button.pack(side=tk.LEFT, padx=5, pady=5)
root.mainloop()
    