import tkinter as tk
from tkinter import mainloop, ttk

root = tk.Tk()
root.geometry('150x150')
root.resizable(False, False)
img = tk.PhotoImage(file='./img_displaying_an_image.png')

# imageで画像を、textで文字を指定。compoundでテキストから見てどちらに画像を表示するか指定する
img_label = ttk.Label(root, image=img, text='this is red square', compound='top').pack() 

root.mainloop()
