import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x300")

# カラムの0番目に対し、1番目は2倍
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=4)

label_1 = ttk.Label(root, text='label_1')
label_1.grid(column=0, row=0, padx=5, pady=5, sticky=tk.W)

entry_1 = ttk.Entry(root)
entry_1.grid(column=1, row=0, padx=5, pady=5, sticky=tk.E)

label_2 = ttk.Label(root, text='label_2')
label_2.grid(column=0, row=1, padx=5, pady=5, sticky=tk.W)

entry_2 = ttk.Entry(root)
entry_2.grid(column=1, row=1, padx=5, pady=5, sticky=tk.E)

root.mainloop()