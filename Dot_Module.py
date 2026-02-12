import tkinter as tk
title = "Dot Module"
def dot_move_up():
    canvas.move(dot, 0, -10)
def dot_move_down():
    canvas.move(dot, 0, 10)
def dot_move_left():
    canvas.move(dot, -10, 0)
def dot_move_right():
    canvas.move(dot, 10, 0)
root = tk.Tk()
root.title(title)
root.geometry("1000x900")
canvas = tk.Canvas(root, width=950, height=600, bg="")
canvas.pack()
dot = canvas.create_oval(190, 140, 210, 160, fill="blue")
button_frame = tk.Frame(root)
button_frame.pack(pady=10)
up_button = tk.Button(button_frame, text="↑", command=dot_move_up)
up_button.grid(row=0, column=1)
down_button = tk.Button(button_frame, text="↓", command=dot_move_down)
down_button.grid(row=2, column=1)
left_button = tk.Button(button_frame, text="←", command=dot_move_left)
left_button.grid(row=1, column=0)
right_button = tk.Button(button_frame, text="→", command=dot_move_right)
right_button.grid(row=1, column=2)
root.mainloop()