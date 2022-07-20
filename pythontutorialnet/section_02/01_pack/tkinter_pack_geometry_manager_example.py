import tkinter as tk

root = tk.Tk()
root.geometry('300x300')

#### box_1 ####
box_1 = tk.Label(
    root,
    text='box_1',
    bg='red',
    fg='white'
)

# # minimal options
# box_1.pack(
#     ipadx=10, # padding to x
#     ipady=10  # padding to y
# )

# # fill to x - 横方向を埋める
# box_1.pack(
#     ipadx=10,
#     ipady=10,
#     fill='x'
# )

# # fill to y - 縦方向を埋めたいが、うまくいかない(後述のexpandを指定すれば意図した通りになる)
# box_1.pack(
#     ipadx=10,
#     ipady=10,
#     fill='y'
# )

# # expand - 他要素のスペースを除いて使用可能な領域を埋める(ただしマージンのようになる)
# box_1.pack(
#     ipadx=10,
#     ipady=10,
#     expand=True
# )

# # expand + fill
# box_1.pack(
#     ipadx=10,
#     ipady=10,
#     fill='both',
#     expand=True
# )

# side - 配置を指定する。省略した場合はtop(=コンテナ上部)
box_1.pack(
    ipadx=10,
    ipady=10,
    fill='both',
    expand=True,
    side='left'
)

#### box_2 ####
box_2 = tk.Label(
    root,
    text='box_2',
    bg='green',
    fg='white'
)
box_2.pack(
    ipadx=10,
    ipady=10
)

root.mainloop()