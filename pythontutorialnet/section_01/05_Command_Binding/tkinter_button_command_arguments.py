import tkinter as tk
from tkinter import ttk

def recieve_arg(option):
    print(f'clicked [{option}]')

root = tk.Tk()

ttk.Button(root, text='hoge', command=lambda: recieve_arg('hoge')).pack()
ttk.Button(root, text='fuga', command=lambda: recieve_arg('fuga')).pack()
ttk.Button(root, text='foobar', command=lambda: recieve_arg('foobar')).pack()

root.mainloop()