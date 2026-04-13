import tkinter as tk

def popup():
    win = tk.Toplevel()
    win.title("Custom Popup")
    win.geometry("300x150")

    label = tk.Label(win, text="Hello! This is a custom popup.")
    label.pack(pady=20)

    btn = tk.Button(win, text="Close", command=win.destroy)
    btn.pack()

root = tk.Tk()
root.withdraw()

root.after(2000, popup)

root.mainloop()
