import tkinter as tk
from tkinter import ttk

root = tk.Tk()

button_enable  = ttk.Button(root, text='enable button')
# button_enable.state(['normal']) # normalについては設定不可。stateを書かなければOK
button_enable.pack()

button_disable = ttk.Button(root, text='disable button')
button_disable.state(['disabled'])
button_disable.pack()

button_remove_disable = ttk.Button(root, text='remove disable button')
button_remove_disable.state(['disabled'])
button_remove_disable.state(['!disabled'])
button_remove_disable.pack()

root.mainloop()