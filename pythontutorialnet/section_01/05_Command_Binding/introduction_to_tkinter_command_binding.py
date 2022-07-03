import tkinter as tk
from tkinter import ttk

# ボタン押下時に呼ばれる(commandに指定される)関数
def button_clicked():
    print('button clicked')

root = tk.Tk()
button = ttk.Button(root, text='Click Me', command=button_clicked) # commandに呼び出したい関数を指定
button.pack()

root.mainloop()