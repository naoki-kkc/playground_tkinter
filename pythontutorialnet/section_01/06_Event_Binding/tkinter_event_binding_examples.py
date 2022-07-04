import tkinter as tk
from tkinter import ttk

def press_return(event):
    print('return pressed')

def press_return_2(event):
    print('return pressed - 2')

def press_tab(event):
    print('return tab')

root   = tk.Tk()
button = ttk.Button(root, text='press return')

# ----- 例1：シンプルなバインド -----
# bindでReturnキーと関数をバインドする
# (注：ボタン押下はバインドされていないので、押しても反応しない)
button.bind('<Return>', press_return)

# ----- 例2：複数のバインド(addなし) -----
# 複数バインド可能だが、同じイベントに対して複数回バインドすると最後が有効になる
"""
button.bind('<Return>', press_return)   # Return押下時に**呼ばれない**
button.bind('<Return>', press_return_2) # Return押下時に呼ばれる
button.bind('<Tab>', press_tab)         # Tab押下時に呼ばれる
"""

# ----- 例3：複数のバインド(add='+') -----
# 第三引数で「add='+'」とした場合、複数回バインドしてもすべて呼び出される
"""
button.bind('<Return>', press_return)
button.bind('<Return>', press_return_2, add='+')
button.bind('<Tab>', press_tab)
"""

# ----- 例4：複数のバインド(add='') -----
# 第三引数で「add=''」とした場合、例2と同じくイベントに対するバインドは最後の宣言となる
"""
button.bind('<Return>', press_return)
button.bind('<Return>', press_return_2, add='')
button.bind('<Tab>', press_tab)
"""

button.focus() # 起動時にフォーカス状態にする
button.pack()
root.mainloop()