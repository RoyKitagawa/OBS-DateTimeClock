import tkinter
import gui_manager as gui

# Tkクラス生成
root = tkinter.Tk()
# 画面サイズ
root.geometry('600x400')
# 画面タイトル
root.title('サンプル画面')

gui.create_date_time_ui(root)


# 画面をそのまま表示
root.mainloop()



