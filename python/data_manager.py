import os

setting_file_name = 'settings.txt'
setting_file_path = './' + setting_file_name

setting_datetime_format = None
setting_font = None
setting_font_size = None
setting_font_color = None
setting_bg_color = None

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

def open_setting_file():
    file = open(setting_file_path, 'a+')
    content_list = file.readlines()

    is_file_empty = True

    length = len(content_list)
    # if(len(file_read) <= 0):
    #     file.write("abcde")
    # else:
    file.write(file_read + "\nabc")
    file.close()