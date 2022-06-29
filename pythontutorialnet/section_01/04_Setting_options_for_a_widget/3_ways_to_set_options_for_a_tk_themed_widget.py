import tkinter as tk
from tkinter import ttk

root = tk.Tk()

# ウィジェット作成時にキーワード引数で設定
# ttk.Label(root, text='text arguments').pack()

# ウィジェット作成後に辞書インデックスで設定
# label_set_dict = ttk.Label(root)
# label_set_dict['text'] = 'set text after create widget by dict'
# label_set_dict.pack()

# ウィジェット作成後にconfig()メソッドで設定
label_set_config = ttk.Label(root)
label_set_config.config(text='set text after create widget by config()')
label_set_config.pack()

root.mainloop()