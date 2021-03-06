import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.geometry('300x300')
root.resizable(False, False)
root.title('image button example')

def img_button_clicked():
    # アラート的なウインドウが表示される
    showinfo(title='info', message='image button clicked')

img_icon   = tk.PhotoImage(file='./download.png')
img_button = ttk.Button(root, image=img_icon, text='Download', compound=tk.LEFT, command=img_button_clicked)
img_button.pack(ipadx=5, ipady=5, expand=True)

root.mainloop()