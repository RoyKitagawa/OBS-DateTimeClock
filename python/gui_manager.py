import tkinter
from tkinter import ttk
from tkinter import colorchooser
from tkhtmlview import HTMLLabel

# 資料
# https://www.python-beginners.com/entry/20210607/1623057987
# 
# 仕様決め
# 1. 時間のフォーマットUI（ドロップダウン）
#       右側に▼ボタン
#       ここには"hh/mm/ss"等の文字列を選択するやつ
#       二行までの文章が入るようにできればベスト
# 2. フォント表示UI
#     右側に「…」ボタン
#     ポップアップ、もしくはドロップダウンからフォントを選択できる形式にしたい
# 3. フォントサイズ
#     まずは全体で１つの固定サイズ
# 4. 文字色
#     表示色の四角を表示（縁取りは黒）
#     色をクリックでカラーピッカー出したいね
# 5. サンプル表示
#     最新の設定をベースに現在日時の時計を実際に表示する

class ColorSelectButton(tkinter.Button):
    def __init__(self, master):
        super().__init__(
            master=master,
            text="",
            width=10,
            relief=tkinter.SOLID,
            bd=1,
            command=self.onclick_color_button,
        )

    def onclick_color_button(self):
        self.config(
            # カラピッカー呼出し後、選択された色の第二要素（色コード）を反映させる
            bg=colorchooser.askcolor()[1]
        )

def create_datetime_sample(root):
    frame = ttk.LabelFrame(root, text="サンプル表示")

    content_frame = ttk.Label(frame,background='#778899')
    content_frame.pack(
        fill=tkinter.BOTH,
        expand=True,
        padx=10,
        pady=(10, 10),
        anchor=tkinter.CENTER,
    )

    # 日時の表示（サンプルのためリアルタイムでなくてOK）
    datetime_label = ttk.Label(content_frame, background='#778899', text="1月23日（金）\n12:34:56.012")
    datetime_label.pack(
        anchor=tkinter.CENTER,
        expand=True,
    )

    frame.pack(
        anchor=tkinter.N,
        fill=tkinter.BOTH,
        padx=10,
        pady=(10, 10),
        expand=True,
    )

def create_background_color(root):
    frame = ttk.Frame(root)

    # Label作成
    title_frame = ttk.Frame(frame, width=110, height=20,)
    ttk.Label(title_frame, text="背景色",).pack(side=tkinter.RIGHT,)
    title_frame.propagate(False)
    title_frame.pack(
        side=tkinter.LEFT,
        padx=(0, 10),
    )

    # カラピッカー用ボタン
    color_button = ColorSelectButton(frame)
    color_button.pack(
        side=tkinter.LEFT,
    )

    frame.pack(
        anchor=tkinter.N,
        fill=tkinter.X,
        padx=10,
        pady=(10, 0),
    )


def create_font_color(root):
    frame = ttk.Frame(root)

    # Label作成
    title_frame = ttk.Frame(frame, width=110, height=20,)
    ttk.Label(title_frame, text="文字色",).pack(side=tkinter.RIGHT,)
    title_frame.propagate(False)
    title_frame.pack(
        side=tkinter.LEFT,
        padx=(0, 10),
    )

    # カラピッカー用ボタン
    color_button = ColorSelectButton(frame)
    # color_button = tkinter.Button(
    #     frame,
    #     text="色",
    #     command=onclick_color_button,
    #     height=1,
    #     width=10,
    #     bg="red",)
    color_button.pack(
        side=tkinter.LEFT,
    )
    # # テキスト入力エリア
    # entry = tkinter.Entry(frame,)
    # entry.pack(
    #     side=tkinter.LEFT,
    # )

    frame.pack(
        anchor=tkinter.N,
        fill=tkinter.X,
        padx=10,
        pady=(10, 0),
    )

def onclick_color_button():
    return

def create_font_size(root):
    frame = ttk.Frame(root)

    # Label作成
    title_frame = ttk.Frame(frame, width=110, height=20,)
    ttk.Label(title_frame, text="フォントサイズ",).pack(side=tkinter.RIGHT,)
    title_frame.propagate(False)
    title_frame.pack(
        side=tkinter.LEFT,
        padx=(0, 10),
    )

    # テキスト入力エリア
    entry = tkinter.Entry(frame,)
    entry.pack(
        side=tkinter.LEFT,
    )

    frame.pack(
        anchor=tkinter.N,
        fill=tkinter.X,
        padx=10,
        pady=(10, 0),
    )


def create_font_ui(root):
    frame = ttk.Frame(root)

    # Label作成
    title_frame = ttk.Frame(frame, width=110, height=20,)
    ttk.Label(title_frame, text="フォント",).pack(side=tkinter.RIGHT,)
    title_frame.propagate(False)
    title_frame.pack(
        side=tkinter.LEFT,
        padx=(0, 10),
    )

    # Combobox自体を作成
    item_list = tkinter.font.families()
    combobox = ttk.Combobox(
        master = frame,
        values = item_list,
    )
    combobox.pack(        
        side=tkinter.LEFT,
        fill=tkinter.X,
        expand=True,
        )
    
    frame.pack(
        anchor=tkinter.N,
        fill=tkinter.X,
        padx=10,
        pady=(10, 0),
    )

def create_date_time_ui(root):
    frame = ttk.Frame(root)

    # Label作成
    title_frame = ttk.Frame(frame, width=110, height=20)
    ttk.Label(title_frame, text="日時表記フォーマット",).pack(side=tkinter.RIGHT,)
    title_frame.propagate(False)
    title_frame.pack(
        side=tkinter.LEFT,
        padx=(0, 10),
    )

    # Combobox自体を作成
    item_list = ["a", "b", "c"]
    combobox = ttk.Combobox(
        master = frame,
        values = item_list,
    )
    combobox.pack(        
        side=tkinter.LEFT,
        fill=tkinter.X,
        expand=True,
        )
    
    frame.pack(
        anchor=tkinter.N,
        fill=tkinter.X,
        padx=10,
        pady=(10, 0),
    )