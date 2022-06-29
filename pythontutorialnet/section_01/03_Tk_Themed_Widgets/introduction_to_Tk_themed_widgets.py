import tkinter as tk
from tkinter import ttk

root = tk.Tk()

# 古典的なウィジェット
tk.Label(root, text='classic label widget').pack()

# Tk8.5で追加された新しいウィジェット
ttk.Label(root, text='themed label widget').pack()

root.mainloop()