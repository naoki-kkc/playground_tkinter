import tkinter as tk

root = tk.Tk()

msg_label = tk.Label(root, text='Hello, world!')
# msg_label = tk.Label(root, text='はろーわーるど') # 日本語でも表示可能
msg_label.pack()

msg_label2 = tk.Label(root, text='invisible widget')
# pack()しないと作成されるが表示されない
# msg_label2.pack()

root.mainloop()