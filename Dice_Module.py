import random
import tkinter as tk

COOLDOWN_TIME = 500  # 0,5 seconds in milliseconds
is_on_cooldown = False


def set_cooldown():
    global is_on_cooldown
    is_on_cooldown = True
    button_roll.config(state=tk.DISABLED)
    button_roll_12.config(state=tk.DISABLED)
    status_bar.config(text="Please stand by...")
    root.after(COOLDOWN_TIME, reset_cooldown)


def reset_cooldown():
    global is_on_cooldown
    is_on_cooldown = False
    button_roll.config(state=tk.NORMAL)
    button_roll_12.config(state=tk.NORMAL)
    status_bar.config(text="Ready to roll!")


def roll_dice():
    if is_on_cooldown:
        return
    result = random.randint(1, 6)
    label_result.config(text=f"You rolled a {result}!")
    set_cooldown()


root = tk.Tk()
root.title("Dice Roller")
root.geometry("300x300")

label_result = tk.Label(
    root, text="Click the button to roll the dice.", font=("Arial", 14)
)
label_result.pack(pady=20)

button_roll = tk.Button(
    root,
    text="Roll the Dice",
    command=roll_dice,
    bg="gray",
    fg="black",
    font=("Arial", 12, "bold"),
)


def twelwe_sided_dice():
    if is_on_cooldown:
        return
    result = random.randint(1, 12)
    label_result.config(text=f"You rolled a {result}!")
    set_cooldown()


button_roll_12 = tk.Button(
    root,
    text="Roll 12-sided Dice",
    command=twelwe_sided_dice,
    bg="gray",
    fg="black",
    font=("Arial", 12, "bold"),
)


def change_style_to_futuristic():
    button_roll.config(bg="black", fg="cyan", font=("Arial", 12, "bold"))
    button_roll_12.config(bg="black", fg="cyan", font=("Arial", 12, "bold"))


button_futuristic = tk.Button(
    root,
    text="Futuristic Style",
    command=change_style_to_futuristic,
    bg="cyan",
    fg="dark gray",
    font=("Arial", 12, "bold"),
)


def change_style_to_classic():
    button_roll.config(bg="gray", fg="black", font=("Arial", 12, "bold"))
    button_roll_12.config(bg="gray", fg="black", font=("Arial", 12, "bold"))


button_classic = tk.Button(
    root,
    text="Classic Style",
    command=change_style_to_classic,
    bg="dark gray",
    fg="cyan",
    font=("Arial", 12, "bold"),
)


status_bar = tk.Label(root, text="Ready to roll!", bd=1, relief=tk.SUNKEN, anchor=tk.W)
status_bar.pack(side=tk.BOTTOM, fill=tk.X)

button_roll.pack()
button_roll_12.pack(pady=10)
button_futuristic.pack(pady=10)
button_classic.pack(pady=10)

root.mainloop()
