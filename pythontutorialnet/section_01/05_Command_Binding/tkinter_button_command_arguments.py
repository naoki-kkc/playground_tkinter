import tkinter as tk
from tkinter import ttk

def recieve_arg(option):
    print(f'clicked [{option}]')

root = tk.Tk()

# 引数を渡す場合はcommandでラムダ式を利用
ttk.Button(root, text='hoge', command=lambda: recieve_arg('hoge')).pack()
ttk.Button(root, text='fuga', command=lambda: recieve_arg('fuga')).pack()
ttk.Button(root, text='foobar', command=lambda: recieve_arg('foobar')).pack()

# 注意：
# ・commandによるバインディングは一部のウィジェットでしか利用できない
# ・ボタンのcommandはreturnにバインドされない
# これらは後述のイベントバインディングで対応する

root.mainloop()