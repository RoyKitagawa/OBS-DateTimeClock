import tkinter
from tkinter import ttk
from ui_class import ColorSelectButton
# import gui_manager as gui
import gui_manager
import data_manager


# 日時表記フォーマット選択UI
datetime_format_frame = None
datetime_format_label_frame = None
datetime_format_label = None
datetime_format_picker = None
datetime_format_list = None

# フォント選択UI
font_frame = None
font_label_frame = None
font_label = None
font_picker = None
font_list = None

# フォントサイズUI
fontsize_frame = None
fontsize_label_frame = None
fontsize_label = None
fontsize_picker = None
fontsize_list = None

# フォント色選択UI
fontcolor_frame = None
fontcolor_label_frame = None
fontcolor_label = None
fontcolor_picker = None

# 背景色選択UI
bgcolor_frame = None
bgcolor_label_frame = None
bgcolor_label = None
bgcolor_picker = None

# 日時のサンプル表示UI
sample_datetime_frame = None
sample_datetime_bg = None
sample_datetime_label = None
sample_datetime_bg_color = '#778899'

# 定数系
text_ui_width = 110
text_ui_height = 20


##############################
# 基本設定
##############################
# Tkクラス生成
root = tkinter.Tk()
# 画面サイズ
root.geometry('600x400')
# 画面タイトル
root.title('サンプル画面')


##############################
# 日時表記フォーマット選択UI
##############################
datetime_format_frame = ttk.Frame(root)

# Label作成
datetime_format_label_frame = ttk.Frame(
    datetime_format_frame, width=text_ui_width, height=text_ui_height)
datetime_format_label = ttk.Label(
    datetime_format_label_frame, text="日時表記フォーマット",)
datetime_format_label.pack(side=tkinter.RIGHT,)
datetime_format_label_frame.propagate(False)
datetime_format_label_frame.pack(side=tkinter.LEFT, padx=(0, 10), )

# Combobox自体を作成
datetime_format_list = ["a", "b", "c"]
datetime_format_picker = ttk.Combobox(
    datetime_format_frame, values=datetime_format_list, )
datetime_format_picker.set(data_manager.load_datetime_format())
datetime_format_picker.pack(side=tkinter.LEFT, fill=tkinter.X, expand=True, )
datetime_format_frame.pack(anchor=tkinter.W, fill=tkinter.X,
                           padx=10,
                           pady=(10, 0),
                           )


##############################
# フォント選択UI
##############################
font_frame = ttk.Frame(root)

# Label作成
font_label_frame = ttk.Frame(font_frame, width=text_ui_width,
                             height=text_ui_height,)
font_label = ttk.Label(font_label_frame, text="フォント",)
font_label.pack(side=tkinter.RIGHT,)
font_label_frame.propagate(False)
font_label_frame.pack(
    side=tkinter.LEFT,
    padx=(0, 10),
)

# Combobox自体を作成
font_list = tkinter.font.families()
font_picker = ttk.Combobox(
    master=font_frame,
    values=font_list,
)
font_picker.set(data_manager.load_font())
font_picker.pack(
    side=tkinter.LEFT,
    fill=tkinter.X,
    expand=True,
)

font_frame.pack(
    anchor=tkinter.W,
    fill=tkinter.X,
    padx=10,
    pady=(10, 0),
)


##############################
# フォントサイズ選択UI
##############################
fontsize_frame = ttk.Frame(root)

# Label作成
fontsize_label_frame = ttk.Frame(fontsize_frame, width=text_ui_width,
                                 height=text_ui_height,)
fontsize_label = ttk.Label(fontsize_label_frame, text="フォントサイズ",)
fontsize_label.pack(side=tkinter.RIGHT,)
fontsize_label_frame.propagate(False)
fontsize_label_frame.pack(
    side=tkinter.LEFT,
    padx=(0, 10),
)

# Combobox自体を作成
fontsize_list = [1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 15, 17, 20, 25, 30, 40, 50, 60,
                 70, 80, 100, 120, 150, 170, 200, 250, 300, 400, 500, 600, 700, 800, 1000, ]
fontsize_picker = ttk.Combobox(
    master=fontsize_frame,
    values=fontsize_list,
)
fontsize_picker.set(data_manager.load_font_size())
fontsize_picker.pack(
    side=tkinter.LEFT,
    # fill=tkinter.X,
    # expand=True,
)
fontsize_frame.pack(
    anchor=tkinter.W,
    # side=tkinter.LEFT,
    # fill=tkinter.X,
    padx=10,
    pady=(10, 0),
)


##############################
# フォント色選択UI
##############################
fontcolor_frame = ttk.Frame(root)

# Label作成
fontcolor_label_frame = ttk.Frame(fontcolor_frame, width=text_ui_width, height=text_ui_height,)
fontcolor_label = ttk.Label(fontcolor_label_frame, text="文字色",)
fontcolor_label.pack(side=tkinter.RIGHT,)
fontcolor_label_frame.propagate(False)
fontcolor_label_frame.pack(
    side=tkinter.LEFT,
    padx=(0, 10),
)

# カラピッカー用ボタン
fontcolor_picker = ColorSelectButton(fontcolor_frame)
fontcolor_picker.set_color(data_manager.load_font_color())
fontcolor_picker.pack(side=tkinter.LEFT, )
fontcolor_frame.pack(
    anchor=tkinter.N,
    fill=tkinter.X,
    padx=10,
    pady=(10, 0),
)


##############################
# 背景色選択UI
##############################
bgcolor_frame = ttk.Frame(root)

# Label作成
bgcolor_label_frame = ttk.Frame(bgcolor_frame, width=text_ui_width, height=text_ui_height,)
bgcolor_label = ttk.Label(bgcolor_label_frame, text="背景色",)
bgcolor_label.pack(side=tkinter.RIGHT,)
bgcolor_label_frame.propagate(False)
bgcolor_label_frame.pack(
    side=tkinter.LEFT,
    padx=(0, 10),
)

# カラピッカー用ボタン
bgcolor_picker = ColorSelectButton(bgcolor_frame)
bgcolor_picker.set_color(data_manager.load_bg_color())
bgcolor_picker.pack(side=tkinter.LEFT, )
bgcolor_frame.pack(
    anchor=tkinter.N,
    fill=tkinter.X,
    padx=10,
    pady=(10, 0),
)


##############################
# サンプル表示UI
# 
# ここのサンプル表示はラベルじゃなくて
# https://self-development.info/%E3%80%90python%E3%80%91tkinter%E3%81%AB%E3%82%88%E3%82%8B%E7%94%BB%E5%83%8F%E8%A1%A8%E7%A4%BA%E3%82%92%E3%82%8F%E3%81%8B%E3%82%8A%E3%82%84%E3%81%99%E3%81%8F%E8%A7%A3%E8%AA%AC/
# https://watlab-blog.com/2021/05/06/decoration-telop/#%E7%B8%81%E5%8F%96%E3%82%8A%E6%96%87%E5%AD%97%E3%82%92%E5%85%A5%E3%82%8C%E3%82%8BPython%E3%82%B3%E3%83%BC%E3%83%89
# https://xn--eckl3qmbc2cv902cnwa746d81h183l.com/instructor-blog/211229how-to-add-bordered-text-to-an-image-in-python/
##############################
sample_datetime_frame = ttk.LabelFrame(root, text="サンプル表示")

sample_datetime_bg = ttk.Label(sample_datetime_frame,background=data_manager.load_bg_color())
sample_datetime_bg.pack(
    fill=tkinter.BOTH,
    expand=True,
    padx=10,
    pady=(10, 10),
    anchor=tkinter.CENTER,
)

# 日時の表示（サンプルのためリアルタイムでなくてOK）
sample_datetime_label = ttk.Label(
    sample_datetime_bg,
    background=data_manager.load_bg_color(),
    text=data_manager.get_sample_datetime_text(),
    foreground=data_manager.load_font_color(),)
sample_datetime_label.pack(
    anchor=tkinter.CENTER,
    expand=True,
)

sample_datetime_frame.pack(
    anchor=tkinter.N,
    fill=tkinter.BOTH,
    padx=10,
    pady=(10, 10),
    expand=True,
)


data_manager.open_setting_file()


# gui = gui_manager.SettingGUI(root)
# gui.initialize()

root.mainloop()

# gui.create_date_time_ui(root)
# gui.create_font_ui(root)
# gui.create_font_size(root)
# gui.create_font_color(root)
# gui.create_background_color(root)
# gui.create_datetime_sample(root)

# gui = gui_manager.SettingGUI(root)
# gui.initialize()

# frame = ttk.Frame()
