import tkinter as tk
from tkinter import messagebox

def repeat_popup():
    messagebox.showinfo("Alert", "This popup repeats every 5 seconds!")
    root.after(5000, repeat_popup)

root = tk.Tk()
root.withdraw()

root.after(5000, repeat_popup)

root.mainloop()
