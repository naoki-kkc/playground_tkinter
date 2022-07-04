import tkinter as tk

def bind_root(event):
    print(f'[{event.keysym}] on root window')

root = tk.Tk()
root.bind('<Any-KeyRelease>', bind_root)
root.mainloop()