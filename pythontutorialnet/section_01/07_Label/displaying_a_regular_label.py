import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('300x100')
root.resizable(False, False)
label = ttk.Label(root, text='label sample').pack()
root.mainloop()