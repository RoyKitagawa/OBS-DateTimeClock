import os
import webbrowser
import tkinter
from tkinter import messagebox
import codecs

setting_file_name = 'settings.txt'
setting_file_path = './' + setting_file_name

##############################
# データ処理用定数
##############################
datetime_format_list = [
    # 日本語版基本セット
    '【1-1】YYYY年MM月DD（aaa） [改行] hh:mm:ss', 
    '【1-2】YYYY年MM月DD（aaa） hh:mm:ss',
    '【1-3】YYYY年MM月DD（aaa）',
    '【1-4】YYYY年MM月DD [改行] hh:mm:ss', 
    '【1-5】YYYY年MM月DD hh:mm:ss',
    '【1-6】YYYY年MM月DD',
    '【1-7】hh:mm:ss',
    # 日本語版基本セット（ミリ秒入り）
    '【2-1】YYYY年MM月DD（aaa） [改行] hh:mm:ss.sss',
    '【2-2】YYYY年MM月DD（aaa） hh:mm:ss.sss',
    '【2-3】YYYY年MM月DD [改行] hh:mm:ss.sss',
    '【2-4】YYYY年MM月DD hh:mm:ss.sss',
    '【2-5】hh:mm:ss.sss',
    # 英語版基本セット
    '【3-1】YYYY/MM/DD (AAA) [改行] hh:mm:ss',
    '【3-2】YYYY/MM/DD (AAA) hh:mm:ss',
    '【3-3】YYYY/MM/DD [改行] hh:mm:ss',
    '【3-4】YYYY/MM/DD hh:mm:ss',
    '【3-5】YYYY/MM/DD',
    # 英語版基本セット（ミリ秒入り）
    '【4-1】YYYY/MM/DD (AAA) [改行] hh:mm:ss.sss',
    '【4-2】YYYY/MM/DD (AAA) hh:mm:ss.sss',
    '【4-3】YYYY/MM/DD [改行] hh:mm:ss.sss',
    '【4-4】YYYY/MM/DD hh:mm:ss.sss',
]

##############################
# データ処理用変数・定数
##############################

#現状使用しているデータ用
data = ['']

data_prefix_date_format = 'DateFormat:'
data_prefix_font = 'Font:'
data_prefix_date_font_size = 'DateFontSize:'
data_prefix_time_font_size = 'TimeFontSize:'
data_prefix_border_size = 'BorderSize:'
data_prefix_text_color = 'TextColor:'
data_prefix_text_border_color = 'TextBorderColor:'
data_prefix_background_color = 'BackgroundColor:'

data_date_format = ''
data_font = ''
data_date_font_size = ''
data_time_font_size = ''
data_border_size = ''
data_text_color = ''
data_text_border_color = ''
data_background_color = ''

initial_date_format = datetime_format_list[0]
initial_date_font_size = '23'
initial_time_font_size = '24'
initial_border_size = '11'
initial_text_color = '#000000'
initial_text_border_color = '#999999'
initial_background_color = '#ffffff'



##############################
# データ処理用関数
##############################
def get_format_datetime_sample(format: str):
    value = None
    base = format.split("】")
    if(len(base) > 1):
        value = base[1]
    else:
        value = base[0]
    
    value = value.replace('YYYY', '1234')
    value = value.replace('MM', '01')
    value = value.replace('DD', '23')
    value = value.replace('HH', '01')
    value = value.replace('hh', '01')
    value = value.replace('mm', '23')
    value = value.replace('sss', '678')
    value = value.replace('ss', '45')
    value = value.replace('ss', '45')
    value = value.replace('aaa', '水')
    value = value.replace('AAA', 'Wed')
    value = value.replace(' [改行] ', '\n')
    value = value.replace(' [改行]', '\n')
    value = value.replace('[改行] ', '\n')
    value = value.replace('[改行]', '\n')

    return value


##############################
# データ読み込み用関数
##############################
def initialize_data():

    # 代入予定のグローバル変数達
    global data
    global data_date_format
    global data_font
    global data_date_font_size
    global data_time_font_size
    global data_border_size
    global data_text_color
    global data_text_border_color
    global data_background_color

    # データ未登録の場合用の強制初期化
    data_date_format = initial_date_format
    data_font = tkinter.font.families()[0]
    data_date_font_size = initial_date_font_size
    data_time_font_size = initial_time_font_size
    data_border_size = initial_border_size
    data_text_color = initial_text_color
    data_text_border_color = initial_text_border_color
    data_background_color = initial_background_color

    # 実際のデータを使って反映処理
    data = read_setting_file()
    # データが空の場合はスルー
    if not data:
        return
    for line in data:
        # 文字列が空の場合はスキップ
        if not line:
            continue
        # ライン別にデータを変数に反映させる
        if line.startswith(data_prefix_date_format):
            data_date_format = remove_data_prefix_and_suffix(line, data_prefix_date_format)
        elif line.startswith(data_prefix_font):
            data_font = remove_data_prefix_and_suffix(line, data_prefix_font)
        elif line.startswith(data_prefix_date_font_size):
            data_date_font_size = remove_data_prefix_and_suffix(line, data_prefix_date_font_size)
        elif line.startswith(data_prefix_time_font_size):
            data_time_font_size = remove_data_prefix_and_suffix(line, data_prefix_time_font_size)
        elif line.startswith(data_prefix_border_size):
            data_border_size = remove_data_prefix_and_suffix(line, data_prefix_border_size)
        elif line.startswith(data_prefix_text_color):
            data_text_color = remove_data_prefix_and_suffix(line, data_prefix_text_color)
        elif line.startswith(data_prefix_text_border_color):
            data_text_border_color = remove_data_prefix_and_suffix(line, data_prefix_text_border_color)
        elif line.startswith(data_prefix_background_color):
            data_background_color = remove_data_prefix_and_suffix(line, data_prefix_background_color)

def remove_data_prefix_and_suffix(data: str, prefix: str):
    data = data.removeprefix(prefix)
    data = data.removesuffix('\n')
    data = data.removesuffix('\r')
    return data

def load_datetime_format():
    return data_date_format

def load_font():
    return data_font

def load_date_font_size():
    return data_date_font_size

def load_time_font_size():
    return data_time_font_size

def load_border_size():
    return data_border_size

def load_text_color():
    return data_text_color

def load_text_border_color():
    return data_text_border_color

def load_background_color():
    return data_background_color


##############################
# データセット用関数
# （変数にのみ反映／ファイルには書き込みしない）
##############################
def set_datetime_format(data: str):
    global data_date_format
    data_date_format = data

def set_font(data: str):
    global data_font
    data_font = data

def set_date_font_size(data: str):
    global data_date_font_size
    data_date_font_size = data

def set_time_font_size(data: str):
    global data_time_font_size
    data_time_font_size = data

def set_border_size(data: str):
    global data_border_size
    data_border_size = data

def set_text_color(data: str):
    global data_text_color
    data_text_color = data

def set_text_border_color(data: str):
    global data_text_border_color
    data_text_border_color = data

def set_background_color(data: str):
    global data_background_color
    data_background_color = data

def update_data():
    global data
    value = data_prefix_date_format + data_date_format + '\n'
    value += data_prefix_font + data_font + '\n'
    value += data_prefix_date_font_size + data_date_font_size + '\n'
    value += data_prefix_time_font_size + data_time_font_size + '\n'
    value += data_prefix_border_size + data_border_size + '\n'
    value += data_prefix_text_color + data_text_color + '\n'
    value += data_prefix_text_border_color + data_text_border_color + '\n'
    value += data_prefix_background_color + data_background_color + '\n'
    data = value

##############################
# ファイル処理用関数
##############################

def is_setting_file_exists():
    return os.path.isfile(setting_file_path)

# def update_datetime_format_sample(text_ui: tkinter.Label):
#     text_ui.text = "AAAAAA"
#     return

def open_datetime_browser():
    webbrowser.open_new_tab("file:///"+ os.path.abspath("./html/clock.html"))

# def apply_setting_from_file():
#     data = read_setting_file
#     if not data:
#         print('Data is empty')
#     else:
#         return

# def set_default_data():
#     return

# def get_sample_datetime_text():
#     return "1月23日（金）\n12:34:56.012"


def read_setting_file(_print_log = False) -> list[str]:
    if not is_setting_file_exists():
        print('No setting file is found')
        return
    
    content_list = None
    with codecs.open(setting_file_path,'r','utf-8') as file:
    # with open(setting_file_path, 'r', "utf-8") as file:
        content_list = file.readlines()

    if(_print_log):
        for line in content_list:
            print(line)

    return content_list

def save_setting_file():
    update_data()
    with codecs.open(setting_file_path,'w','utf-8') as file:
    # with open(setting_file_path, 'w', "utf-8") as file:
        for line in data:
            # 文字列が空の場合はスキップ
            if not line:
                continue
            file.write(line)

    messagebox.showinfo('お知らせ', '設定が保存されました')
    

# def open_setting_file():
#     with open(setting_file_path, 'r') as file:

    # file = open(setting_file_path, 'a+')
    # content_list = file.readlines()

    # is_file_empty = True

    # length = len(content_list)
    # file.close()
    #     # # if(len(file_read) <= 0):
    # # #     file.write("abcde")
    # # # else:
    # # file.write(file_read + "\nabc")
