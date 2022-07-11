import tkinter as tk
from tkinter import ttk

# ウインドウの初期化
root = tk.Tk()
root.geometry('300x300')
root.resizable(False, False)
root.title('button example')

# ボタン追加
sample_button = ttk.Button(root, text='exit', command=lambda: root.quit())
sample_button.pack(ipadx=5, ipady=5, expand=True)\

root.mainloop()