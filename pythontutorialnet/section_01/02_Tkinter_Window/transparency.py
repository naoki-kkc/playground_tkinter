import tkinter as tk

root = tk.Tk()
root.title('Tkinter transparency demo')
root.geometry('500x300+50+50')
root.resizable(False, False)

# 透明度の設定
root.attributes('-alpha', 0.5) # 設定可能な範囲は0.0～1.0

root.mainloop()