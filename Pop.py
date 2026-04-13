import tkinter as tk
from tkinter import messagebox

def show_popup():
    messagebox.showinfo("Reminder", "This popup appeared after 3 seconds!")

root = tk.Tk()
root.withdraw()

# Delay of 3000 ms (3 seconds)
root.after(3000, show_popup)

root.mainloop()
