import tkinter as tk
from tkinter import ttk

def press_b_lower(event):
    print('lower b')

def press_b_upper(event):
    print('UPPER B')

def release_up(event):
    print('↑')

def release_down(event):
    print('↓')

def release_right(event):
    print('→')

def release_left(event):
    print('←')

def release_c_a_a(event):
    print('control + alt + a')

def release_s_u(event):
    print('shift + ↑')

def release_any(event):
    print(f'any key [{event.keysym}]')

root   = tk.Tk()

# バインドする際は以下の表記で行う
# <eventmodifier-eventtype-eventdetail>

# ----- 例1：bキー(キー押下しっぱなしで複数回入力) -----
"""
button = ttk.Button(root, text='plz press b or B')
button.bind('<KeyPress-b>', press_b_lower) # 小文字b
button.bind('<KeyPress-B>', press_b_upper) # 大文字B
"""

# ----- 例2：方向キー(キーが解放で1回入力) -----
"""
button = ttk.Button(root, text='plz press and release any arrow key')
button.bind('<KeyRelease-Up>', release_up)
button.bind('<KeyRelease-Down>', release_down)
button.bind('<KeyRelease-Right>', release_right)
button.bind('<KeyRelease-Left>', release_left)
"""

# ----- 例3：Control + alt + a (aキー解放で1回入力) -----
"""
button = ttk.Button(root, text='plz press and release [Control + alt + a]')
button.bind('<Alt-Control-KeyRelease-a>', release_c_a_a)
"""

# ----- 例4：shift + ↑ (キーが解放で1回入力) -----
"""
button = ttk.Button(root, text='plz press and release [shift + ↑]')
button.bind('<Shift-KeyRelease-Up>', release_s_u)
"""

# ----- 例5：press any key -----
button = ttk.Button(root, text='plz press any key')
button.bind('<Any-KeyRelease>', release_any)

button.focus()
button.pack()
root.mainloop()