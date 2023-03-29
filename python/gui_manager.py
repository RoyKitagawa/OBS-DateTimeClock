from tkinter import ttk

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


def create_date_time_ui(root):
    
    item_list = ["a", "b", "c"]
    combobox = ttk.Combobox(
        master = root,
        values = item_list,
    )
    return