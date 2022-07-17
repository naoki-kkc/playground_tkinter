import tkinter as tk
from tkinter import ttk

root = tk.Tk()

passwd_str   = tk.StringVar()
passwd_entry = ttk.Entry(root, textvariable=passwd_str, show='*')
# passwd_entry = ttk.Entry(root, textvariable=passwd_str, show='●') # どっちかというとこっちの方がよくみる気がする
passwd_entry.pack()

root.mainloop()