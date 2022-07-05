import tkinter as tk
from tkinter import ttk

root = tk.Tk()
label_1 = ttk.Label(root, text='this is Helvetica - 20pt font', font=('Helvetica', 20)).pack()
label_2 = ttk.Label(root, text='this is Meiryo UI - 14pt font', font=('Meiryo UI', 14)).pack()


root.mainloop()