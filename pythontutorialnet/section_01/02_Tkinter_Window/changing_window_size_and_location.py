import tkinter as tk

root = tk.Tk()
root.title('Tkinter Window Geometry')

# 1.geometryの設定値(原点は画面左上)
# height      = '600'
# width       = '400'
# margin_top  = '50'
# margin_left = '50'

# 2.ウインドウを中央に配置したい場合
height        = '600'
width         = '400'
## 画面のサイズを取得
screen_width  = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
print(f'screen_width  : {screen_width}')
print(f'screen_height : {screen_height}')
## 中央にするためのマージンを計算
margin_top  = int(screen_width / 2 - int(width) / 2)
margin_left = int(screen_height / 2 - int(height) / 2)
print(f'margin_top    : {margin_top} ({screen_width} / 2 - {width} / 2)')
print(f'margin_left   : {margin_left} ({screen_height} / 2 - {height} / 2)')


# 上記値からgeometryに設定する文字列を生成
geometry = f'{height}x{width}+{margin_top}+{margin_left}'
print('create geometry : ' + geometry)

# 生成した文字列をgeometryに設定
root.geometry(geometry)

root.mainloop()