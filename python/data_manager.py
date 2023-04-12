import os
import webbrowser
import tkinter

setting_file_name = 'settings.txt'
setting_file_path = './' + setting_file_name

##############################
# データキャッシュ用変数
##############################
setting_datetime_format = None
setting_font = None
setting_font_size = None
setting_font_color = None
setting_bg_color = None

##############################
# データ処理用定数
##############################
datetime_format_sample = [
    # 日本語版基本セット
    '1-1. YYYY年MM月DD（aaa） [改行] hh:mm:ss', 
    '1-2. YYYY年MM月DD（aaa） hh:mm:ss',
    '1-3. YYYY年MM月DD（aaa）',
    '1-4. YYYY年MM月DD [改行] hh:mm:ss', 
    '1-5. YYYY年MM月DD hh:mm:ss',
    '1-6. YYYY年MM月DD',
    '1-7. hh:mm:ss',
    # 日本語版基本セット（ミリ秒入り）
    '2-1. YYYY年MM月DD（aaa） [改行] hh:mm:ss.sss',
    '2-2. YYYY年MM月DD（aaa） hh:mm:ss.sss',
    '2-3. YYYY年MM月DD [改行] hh:mm:ss.sss',
    '2-4. YYYY年MM月DD hh:mm:ss.sss',
    '2-5. hh:mm:ss.sss',
    # 英語版基本セット
    '3-1. YYYY/MM/DD (aaa) [改行] hh:mm:ss',
    '3-2. YYYY/MM/DD (aaa) hh:mm:ss',
    '3-3. YYYY/MM/DD [改行] hh:mm:ss',
    '3-4. YYYY/MM/DD hh:mm:ss',
    '3-5. YYYY/MM/DD',
    # 英語版基本セット（ミリ秒入り）
    '4-1. YYYY/MM/DD (aaa) [改行] hh:mm:ss.sss',
    '4-2. YYYY/MM/DD (aaa) hh:mm:ss.sss',
    '4-3. YYYY/MM/DD [改行] hh:mm:ss.sss',
    '4-4. YYYY/MM/DD hh:mm:ss.sss',
]

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


def load_datetime_format():
    return 'hh:mm:ss'

def load_font():
    return '瀞ノグリッチ明朝 H1'

def load_font_size():
    return '30'

def load_font_color():
    return '#778899'

def load_bg_color():
    return '#ff8899'

def get_sample_datetime_text():
    return "1月23日（金）\n12:34:56.012"

def is_setting_file_exists():
    return os.path.isfile(setting_file_path)

def update_datetime_format_sample(text_ui: tkinter.Label):
    text_ui.text = "AAAAAA"
    return

def open_datetime_browser():
    webbrowser.open_new_tab("file:///"+ os.path.abspath("./html/clock.html"))

def read_setting_file(_print_log = False):
    content_list = None
    with open(setting_file_path, 'r') as file:
        content_list = file.readlines()

    if(_print_log):
        for line in content_list:
            print(line)

    return content_list

def save_setting_file():
    return

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
