import tkinter
from tkinter import ttk
import gui_manager as gui

# Tkクラス生成
root = tkinter.Tk()
# 画面サイズ
root.geometry('600x400')
# 画面タイトル
root.title('サンプル画面')

gui.create_date_time_ui(root)
gui.create_font_ui(root)
gui.create_font_size(root)
gui.create_font_color(root)
gui.create_background_color(root)
gui.create_datetime_sample(root)

frame = ttk.Frame(root)

# 画面をそのまま表示
root.mainloop()



