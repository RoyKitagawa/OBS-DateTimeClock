import tkinter
from tkinter import ttk
from tkinter import colorchooser
from tkhtmlview import HTMLLabel

class SettingGUI():
    def __init__(self, root, ):
        self.root = root,

        # 日時表記フォーマット選択UI
        self.datetime_format_frame = None,
        self.datetime_format_label = None,
        self.datetime_format_picker = None,
        
        # フォント選択UI
        self.font_frame = None,
        self.font_picker = None,

        # フォントサイズUI
        self.fontsize_frame = None,
        self.fontise_label = None,

        # フォント色選択UI
        self.fontcolor_frame = None,
        self.fontcolor_picker = None,

        # 背景色選択UI
        self.bgcolor_frame = None,
        self.bgcolor_picker = None,

        # 日時のサンプル表示UI
        self.datetime_frame = None,
        self.datetime_bg = None,
        self.datetime_label = None,
        self.datetime_bg_color = '#778899',

        # 表示テスト用
        self.sample_label = None,
        
        # 定数系
        self.text_ui_width = 110,
        self.text_ui_height = 20,
        return
    
    def initialize(self):
        # # 日時表記フォーマット選択UI
        # self.datetime_format_frame = ttk.Frame(self.root)
        # self.datetime_format_label_frame = ttk.Frame(
        #     self.datetime_format_frame,
        #     width = self.text_ui_width,
        #     height = self.text_ui_height,
        # ).propagate(False)
        # # 日時表記フォーマットのラベル部分
        # self.datetime_format_label = ttk.Label(
        #     self.datetime_format_label_frame,
        #     text = "日時表記フォーマット",
        # ).pack(side=tkinter.RIGHT)
        # self.datetime_format_label_frame.pack(
        #     side = tkinter.LEFT,
        #     padx = (0, 10),
        # )
        return

    