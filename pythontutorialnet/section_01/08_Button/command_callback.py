import tkinter as tk
from tkinter import ttk

root = tk.Tk()

def callback():
    print('callback fired')

ttk.Button(root, text='callback button', command=callback).pack()

root.mainloop()