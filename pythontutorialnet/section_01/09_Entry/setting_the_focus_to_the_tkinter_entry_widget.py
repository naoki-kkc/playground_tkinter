import tkinter as tk
from tkinter import ttk

root = tk.Tk()

text_1    = tk.StringVar()
textbox_1 = ttk.Entry(root, textvariable=text_1)
textbox_1.pack()
text_1.set('this is not focus')


text_2    = tk.StringVar()
textbox_2 = ttk.Entry(root, textvariable=text_2)
textbox_2.pack()
textbox_2.focus()
text_2.set('THIS IS FOCUS')

root.mainloop()