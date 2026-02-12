import tkinter as tk


def main():
    root = tk.Tk()
    root.title("Test Module")
    root.geometry("320x140")

    label = tk.Label(root, text="Test Module", font=("Arial", 16))
    label.pack(pady=16)

    btn_close = tk.Button(root, text="Close", command=root.destroy)
    btn_close.pack()
    root.mainloop()


if __name__ == "__main__":
    main()
