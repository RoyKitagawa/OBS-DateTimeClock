import tkinter
from tkinter import ttk
from ui_class import ColorSelectButton
# import gui_manager as gui
import gui_manager
import data_manager
from tkinter import colorchooser

# 日時表記フォーマット選択UI
datetime_format_frame = None
datetime_format_label_frame = None
datetime_format_label = None
datetime_format_picker = None
datetime_format_list = None

# 日付表記サンプルUI
datetime_sample_label = None
sample_label_text = None

# フォント選択UI
font_frame = None
font_label_frame = None
font_label = None
font_picker = None
font_list = None

# 日付フォントサイズUI
datefontsize_frame = None
datefontsize_label_frame = None
datefontsize_label = None
datefontsize_picker = None
datefontsize_list = None

# 時間のフォントサイズUI
timefontsize_frame = None
timefontsize_label_frame = None
timefontsize_label = None
timefontsize_picker = None
timefontsize_list = None

# 縁取りのサイズ
fontbordersize_picker = None

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

# フォント縁色選択UI
fontbordercolor_picker = None

# 日時のサンプル表示UI
sample_datetime_frame = None
sample_datetime_bg = None
sample_datetime_label = None
sample_datetime_bg_color = '#778899'

# 定数系
text_ui_width = 110
text_ui_height = 20

##############################
# 設定変更反映用のコールバック処理
##############################

# 日付フォーマット変更時
def on_datetime_format_select(event):
    selected_format = data_manager.datetime_format_list[datetime_format_picker.current()]
    datetime_sample_label['text'] = data_manager.get_format_datetime_sample(selected_format)
    data_manager.set_datetime_format(selected_format)

# フォント変更時
def on_font_select(event):
    selected_data = data_manager.get_font_list()[font_picker.current()]
    data_manager.set_font(selected_data)

# 日付フォントサイズ変更時
def on_date_font_size_select(event):
    selected_data = data_manager.fontsize_list[datefontsize_picker.current()]
    data_manager.set_date_font_size(str(selected_data))

# 時間フォントサイズ変更時
def on_time_font_size_select(event):
    selected_data = data_manager.fontsize_list[timefontsize_picker.current()]
    data_manager.set_time_font_size(str(selected_data))

# 縁取りフォントサイズ変更時
def on_border_size_select(event):
    selected_data = data_manager.fontsize_list[fontbordersize_picker.current()]
    data_manager.set_border_size(str(selected_data))

# 文字色変更時
def on_text_color_select():
    global fontcolor_picker
    color = colorchooser.askcolor()[1]
    fontcolor_picker['bg'] = color
    data_manager.set_text_color(color)

# 文字縁取り色変更時
def on_border_color_select():
    global fontbordercolor_picker
    color = colorchooser.askcolor()[1]
    fontbordercolor_picker['bg'] = color
    data_manager.set_text_border_color(color)

# 背景色
def on_background_color_select():
    global bgcolor_picker
    color = colorchooser.askcolor()[1]
    bgcolor_picker['bg'] = color
    data_manager.set_background_color(color)

##############################
# 基本設定
##############################
# Tkクラス生成
root = tkinter.Tk()
# 画面サイズ
root.geometry('600x400')
# 画面タイトル
root.title('OBS時計設定')

# データの初期化処理
data_manager.initialize_data()

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
datetime_format_picker = ttk.Combobox(
    datetime_format_frame, values=data_manager.datetime_format_list, )
datetime_format_picker.set(data_manager.load_datetime_format())
datetime_format_picker.bind('<<ComboboxSelected>>', on_datetime_format_select)
datetime_format_picker.pack(side=tkinter.LEFT, fill=tkinter.X, expand=True, )
datetime_format_frame.pack(anchor=tkinter.W, fill=tkinter.X,
                           padx=10,
                           pady=(10, 0),
                           )

##############################
# 日時表記フォーマットサンプル表示UI
##############################
datetime_sample_frame = ttk.Frame(root)

# Label作成
datetime_sample_title_label_frame = ttk.Frame(
    datetime_sample_frame, width=text_ui_width, height=text_ui_height)
datetime_sample_title_label = ttk.Label(
    datetime_sample_title_label_frame, text="日時表記サンプル",)
datetime_sample_title_label.pack(side=tkinter.RIGHT,)
datetime_sample_title_label_frame.propagate(False)
datetime_sample_title_label_frame.pack(side=tkinter.LEFT, padx=(0, 10), )

# Label作成
datetime_sample_label_frame = ttk.Frame(datetime_sample_frame, width=text_ui_width, height=text_ui_height*2, relief=tkinter.SOLID)
datetime_sample_label = ttk.Label(datetime_sample_label_frame, text="aaaaaa",)
datetime_sample_label.pack(side=tkinter.LEFT, padx=(10, 10))

datetime_sample_label_frame.propagate(False)
datetime_sample_label_frame.pack(
    side=tkinter.LEFT,
    padx=(0, 10),
    fill=tkinter.X,
    expand=True,
)

datetime_sample_frame.pack(anchor=tkinter.W, fill=tkinter.X,
                           padx=10,
                           pady=(10, 0),
                           )
on_datetime_format_select(None)



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
font_picker = ttk.Combobox(
    master=font_frame,
    values=data_manager.get_font_list(),
)
font_picker.set(data_manager.load_font())
font_picker.bind('<<ComboboxSelected>>', on_font_select)
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
# 日付のフォントサイズ選択UI
##############################
datefontsize_frame = ttk.Frame(root)

# Label作成
datefontsize_label_frame = ttk.Frame(datefontsize_frame, width=text_ui_width,
                                 height=text_ui_height,)
datefontsize_label = ttk.Label(datefontsize_label_frame, text="日付フォントサイズ",)
datefontsize_label.pack(side=tkinter.RIGHT,)
datefontsize_label_frame.propagate(False)
datefontsize_label_frame.pack(
    side=tkinter.LEFT,
    padx=(0, 10),
)

# Combobox自体を作成
datefontsize_picker = ttk.Combobox(
    master=datefontsize_frame,
    values=data_manager.fontsize_list,
)
datefontsize_picker.set(data_manager.load_date_font_size())
datefontsize_picker.bind('<<ComboboxSelected>>', on_date_font_size_select)
datefontsize_picker.pack(
    side=tkinter.LEFT,
    # fill=tkinter.X,
    # expand=True,
)
datefontsize_frame.pack(
    anchor=tkinter.W,
    # side=tkinter.LEFT,
    # fill=tkinter.X,
    padx=10,
    pady=(10, 0),
)

##############################
# 時間のフォントサイズ選択UI
##############################
timefontsize_frame = ttk.Frame(root)

# Label作成
timefontsize_label_frame = ttk.Frame(timefontsize_frame, width=text_ui_width,
                                 height=text_ui_height,)
timefontsize_label = ttk.Label(timefontsize_label_frame, text="時間フォントサイズ",)
timefontsize_label.pack(side=tkinter.RIGHT,)
timefontsize_label_frame.propagate(False)
timefontsize_label_frame.pack(
    side=tkinter.LEFT,
    padx=(0, 10),
)

# Combobox自体を作成
timefontsize_picker = ttk.Combobox(
    master=timefontsize_frame,
    values=data_manager.fontsize_list,
)
timefontsize_picker.set(data_manager.load_time_font_size())
timefontsize_picker.bind('<<ComboboxSelected>>', on_time_font_size_select)
timefontsize_picker.pack(
    side=tkinter.LEFT,
    # fill=tkinter.X,
    # expand=True,
)
timefontsize_frame.pack(
    anchor=tkinter.W,
    # side=tkinter.LEFT,
    # fill=tkinter.X,
    padx=10,
    pady=(10, 0),
)

##############################
# 縁取りののフォントサイズ選択UI
##############################
fontbordersize_frame = ttk.Frame(root)

# Label作成
fontbordersize_label_frame = ttk.Frame(fontbordersize_frame, width=text_ui_width,
                                 height=text_ui_height,)
fontbordersize_label = ttk.Label(fontbordersize_label_frame, text="縁取りサイズ",)
fontbordersize_label.pack(side=tkinter.RIGHT,)
fontbordersize_label_frame.propagate(False)
fontbordersize_label_frame.pack(
    side=tkinter.LEFT,
    padx=(0, 10),
)

# Combobox自体を作成
fontbordersize_picker = ttk.Combobox(
    master=fontbordersize_frame,
    values=data_manager.fontsize_list,
)
fontbordersize_picker.set(data_manager.load_border_size())
fontbordersize_picker.bind('<<ComboboxSelected>>', on_border_size_select)
fontbordersize_picker.pack(
    side=tkinter.LEFT,
    # fill=tkinter.X,
    # expand=True,
)
fontbordersize_frame.pack(
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
fontcolor_picker = tkinter.Button(fontcolor_frame,text="", width=10, relief=tkinter.SOLID, bd=1)
fontcolor_picker['bg'] = data_manager.load_text_color()
fontcolor_picker['command'] = on_text_color_select
fontcolor_picker.pack(side=tkinter.LEFT, )
fontcolor_frame.pack(
    anchor=tkinter.N,
    fill=tkinter.X,
    padx=10,
    pady=(10, 0),
)

##############################
# 縁取り色選択UI
##############################
fontbordercolor_frame = ttk.Frame(root)

# Label作成
fontbordercolor_label_frame = ttk.Frame(fontbordercolor_frame, width=text_ui_width, height=text_ui_height,)
fontbordercolor_label = ttk.Label(fontbordercolor_label_frame, text="文字の縁取り色",)
fontbordercolor_label.pack(side=tkinter.RIGHT,)
fontbordercolor_label_frame.propagate(False)
fontbordercolor_label_frame.pack(
    side=tkinter.LEFT,
    padx=(0, 10),
)

# カラピッカー用ボタン
fontbordercolor_picker = tkinter.Button(fontbordercolor_frame,text="", width=10, relief=tkinter.SOLID, bd=1)
fontbordercolor_picker['bg'] = data_manager.load_text_border_color()
fontbordercolor_picker['command'] = on_border_color_select
fontbordercolor_picker.pack(side=tkinter.LEFT, )
fontbordercolor_frame.pack(
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
bgcolor_picker = tkinter.Button(bgcolor_frame,text="", width=10, relief=tkinter.SOLID, bd=1)
bgcolor_picker['bg'] = data_manager.load_background_color()
bgcolor_picker['command'] = on_background_color_select
bgcolor_picker.pack(side=tkinter.LEFT, )
bgcolor_frame.pack(
    anchor=tkinter.N,
    fill=tkinter.X,
    padx=10,
    pady=(10, 0),
)

##############################
# サンプルHTML起動
##############################
preview_frame = ttk.Frame(root)

# Label作成
preview_label_frame = ttk.Frame(preview_frame, width=text_ui_width, height=text_ui_height,)
preview_label = ttk.Label(preview_label_frame, text="プレビュー",)
preview_label.pack(side=tkinter.RIGHT,)
preview_label_frame.propagate(False)
preview_label_frame.pack(
    side=tkinter.LEFT,
    padx=(0, 10),
)

preview_button = ttk.Button(
    preview_frame,
    text="プレビューを表示する",
    command=data_manager.open_datetime_browser)
# preview_button.set_color(data_manager.load_bg_color())
preview_button.pack(
    side=tkinter.LEFT,
    expand=True,
    fill=tkinter.X,)
preview_frame.pack(
    anchor=tkinter.N,
    fill=tkinter.X,
    padx=10,
    pady=(10, 0),
)

##############################
# 保存する
##############################
save_frame = ttk.Frame(root)

# Label作成
save_label_frame = ttk.Frame(save_frame, width=text_ui_width, height=text_ui_height,)
save_label = ttk.Label(save_label_frame, text="保存",)
save_label.pack(side=tkinter.RIGHT,)
save_label_frame.propagate(False)
save_label_frame.pack(
    side=tkinter.LEFT,
    padx=(0, 10),
)


save_button = ttk.Button(
    save_frame,
    text="設定を保存する",
    command=data_manager.save_setting_file)
save_button.pack(
    side=tkinter.LEFT,
    expand=True,
    fill=tkinter.X,)
save_frame.pack(
    anchor=tkinter.N,
    fill=tkinter.X,
    padx=10,
    pady=(10, 0),
)


# timefontsize_picker.set(data_manager.load_font_size())
# timefontsize_picker.pack(
#     side=tkinter.LEFT,
#     # fill=tkinter.X,
#     # expand=True,
# )
# timefontsize_frame.pack(
#     anchor=tkinter.W,
#     # side=tkinter.LEFT,
#     # fill=tkinter.X,
#     padx=10,
#     pady=(10, 0),
# )

# ##############################
# # サンプル表示UI
# # 
# # ここのサンプル表示はラベルじゃなくて
# # https://self-development.info/%E3%80%90python%E3%80%91tkinter%E3%81%AB%E3%82%88%E3%82%8B%E7%94%BB%E5%83%8F%E8%A1%A8%E7%A4%BA%E3%82%92%E3%82%8F%E3%81%8B%E3%82%8A%E3%82%84%E3%81%99%E3%81%8F%E8%A7%A3%E8%AA%AC/
# # https://watlab-blog.com/2021/05/06/decoration-telop/#%E7%B8%81%E5%8F%96%E3%82%8A%E6%96%87%E5%AD%97%E3%82%92%E5%85%A5%E3%82%8C%E3%82%8BPython%E3%82%B3%E3%83%BC%E3%83%89
# # https://xn--eckl3qmbc2cv902cnwa746d81h183l.com/instructor-blog/211229how-to-add-bordered-text-to-an-image-in-python/
# ##############################
# sample_datetime_frame = ttk.LabelFrame(root, text="サンプル表示")

# sample_datetime_bg = ttk.Label(sample_datetime_frame,background=data_manager.load_bg_color())
# sample_datetime_bg.pack(
#     fill=tkinter.BOTH,
#     expand=True,
#     padx=10,
#     pady=(10, 10),
#     anchor=tkinter.CENTER,
# )

# # 日時の表示（サンプルのためリアルタイムでなくてOK）
# sample_datetime_label = ttk.Label(
#     sample_datetime_bg,
#     background=data_manager.load_bg_color(),
#     text=data_manager.get_sample_datetime_text(),
#     foreground=data_manager.load_font_color(),)
# sample_datetime_label.pack(
#     anchor=tkinter.CENTER,
#     expand=True,
# )

# sample_datetime_frame.pack(
#     anchor=tkinter.N,
#     fill=tkinter.BOTH,
#     padx=10,
#     pady=(10, 10),
#     expand=True,
# )





# # data_manager.open_setting_file()


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
