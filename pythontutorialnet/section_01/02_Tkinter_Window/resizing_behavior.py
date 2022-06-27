import tkinter as tk

root = tk.Tk()
root.title('Tkinter Resize Demo')
root.geometry('1000x500+50+50')

# リサイズ可能
root.resizable(True, True)

# 横のみリサイズ可能
# root.resizable(True, False)

# 縦のみリサイズ可能
# root.resizable(False, True)

# リサイズ不可
# root.resizable(False, False)

# リサイズ可能な範囲を設定
root.minsize(500, 250)  # 下限(下限がgeometryで設定されていたサイズより大きい場合、下限が優先される模様)
root.maxsize(1500, 1000) # 上限

root.mainloop()