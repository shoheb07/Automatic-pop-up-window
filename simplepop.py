import tkinter as tk
from tkinter import messagebox

# Create main window (hidden)
root = tk.Tk()
root.withdraw()

# Show popup
messagebox.showinfo("Popup Title", "This is an automatic popup window!")

# Close app
root.destroy()
