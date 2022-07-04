import tkinter as tk
from tkinter import ttk

def paste(event):
    print('paste called!')

root = tk.Tk()

entry_1 = tk.Entry(root).pack()
entry_2 = tk.Entry(root).pack()
entry_3 = tk.Entry(root).pack()

# サンプルコードだと動かなかった
# root.bind_class('Entry', '<Control-V>', paste) # ctrl + vと見せかけて実質的にはctrl + shift + v
root.bind_class('Entry', '<Control-v>', paste)   # vを小文字にして解決

root.mainloop()