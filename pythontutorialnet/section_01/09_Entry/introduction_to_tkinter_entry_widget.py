import tkinter as tk
from tkinter import ttk

root = tk.Tk()

text    = tk.StringVar()
textbox = ttk.Entry(root, textvariable=text)
textbox.pack()

def print_textbox():
    print(text.get())

ttk.Button(root, text='print_textbox', command=print_textbox).pack()

def set_textbox():
    text.set('hoge')

ttk.Button(root, text='set_textbox_hoge', command=set_textbox).pack()

root.mainloop()