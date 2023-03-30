import tkinter
from tkinter import colorchooser

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

    def set_color(self, color_code, ):
        self.config(
            bg=color_code,            
        )
