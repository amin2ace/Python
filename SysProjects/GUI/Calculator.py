import tkinter as t
from tkinter.font import Font
from tkinter import ttk, END
from typing import Callable
from math import sqrt, pow, ceil, floor


class Calculator(t.Tk):
    def __init__(self, screenName: str | None = None, baseName: str | None = None, className: str = "Tk",
                useTk: bool = True, sync: bool = False, use: str | None = None) -> None:
        super().__init__("Calculator", baseName, className, useTk, sync, use)
        self.title(screenName)
        get_window_geo: tuple[int] = self.winfo_screenwidth(), self.winfo_screenheight()
        self.width: int = 588; self.height: int = 540
        geometry: str = f"{self.width}x{self.height}+{get_window_geo[0]//2 - self.width//2}+{get_window_geo[1]//2 - self.height//2}"
        self.geometry(geometry)
        self.resizable(False, False)
        self.style = ttk.Style(self)

        ### Fonts
        btns_font: Font = Font(family='centry', weight='bold', size=14)
        ent_font: Font = Font(family='calibri', size=16)
        his_font: Font = Font(family='centry', size=8)

        ### Entry Pane
        self.ent_pane: t.PanedWindow = t.PanedWindow(self, width=100)
        self.entry: t.Entry = t.Entry(self.ent_pane, width=38, borderwidth=3, font=ent_font)
        self.ent_pane.grid(column=0, row=0)
        self.entry.grid(column=0, row=1)
        ### Unicode character for buttons
        self.plus: str = '\u2795'; self.mine: str = '\u2796'; self.mult: str = '\u2716'; self.divi: str = '\u2797'
        self.sqrr: str = '\u221A'; self.back: str = '\u2190'; self.perc: str = '\u0025'; self.abss: str = '\u00B1'
        btn_list = [self.perc, 'CH', 'c', self.back,
                    '1/x', 'Pow', self.sqrr, self.divi,
                    '7', '8', '9', self.mult,
                    '4', '5', '6', self.mine,
                    '1', '2', '3', self.plus,
                    self.abss, '0', '.', '=']
        ### Buttons Pane
        self.btn_pane: t.PanedWindow = t.PanedWindow(self, width=100)
        self.btn_pane.grid(column=0, row=1)
        self.btns: list[t.Button] = []
        col, ro = 0, 0
        for index, btn in enumerate(btn_list):
            self.btns.append(t.Button(self.btn_pane, text=btn, font=btns_font, borderwidth=2, width=8, height=3,
                                      command=lambda x=btn: self.get_btns(x)).grid(column=col, row=ro))
            col += 1
            if col >= 4: col, ro = 0, ro + 1

        
        # print(self.btns)
        ### History Pane
        self.his_pane: t.PanedWindow = t.PanedWindow(self, width=50, height=30)
        self.his_frame: t.LabelFrame = t.LabelFrame(self.his_pane, text='History', width=50, font=his_font, padx=10, height=30)
        self.his_label: t.Label = t.Label(self.his_frame, font=his_font, justify='right', height=30, width=20)
        self.his_pane.grid(column=1, row=0, padx=6, rowspan=2)
        self.his_frame.grid(column=0, row=0, sticky='n')
        self.his_label.grid(column=0, row=0, sticky='ne')
        # print(self.btn_pane.size())
        # print(self.size())


        self.mainloop()

    def get_btns(self, name: str) -> Callable:
        try:
            if name in '0123456789.': self.get_numbers(name)
            elif name in 'Xc': self.clear(name)
            elif name in 'CH': self.history_clear()
            elif name in '=': self.operation()
            else: self.get_operand(name)

        except AssertionError:
            print("Enter Number First...")
    def get_numbers(self, number: str):
        self.entry.insert(END, number)

    def get_operand(self, operand: str):
        global sqrr
        self.first_number: str = self.entry.get()
        self.operand: str = operand
        print(self.operand)
        self.history_insert(self.first_number)
        self.entry.delete(0, END)
        self.history_insert(operand)
        if operand == '1/x' or operand == self.sqrr : self.operation()
        
    def clear(self, operand: str = 'c'):
        x = self.entry.get()
        self.entry.delete(0,END)
        if operand == 'X':
            self.entry.insert(0, x[:-1])

    def history_insert(self, insertion: str):
        self.his_label['text'] += f'{insertion}\n'
        ...
    def history_clear(self):
        self.his_label.config(text='')
        ...
    def operation(self):
        second_number: str = self.entry.get()
        result: str = 0
        self.entry.delete(0,END)
        self.history_insert(second_number)
        if self.operand == self.plus:
            result = f'{float(self.first_number)+float(second_number):.5f}'
        elif self.operand == self.mine:
            result = f'{float(self.first_number)-float(second_number):.5f}'
        elif self.operand == self.mult:
            result = f'{float(self.first_number)*float(second_number):.7f}'
        elif self.operand == self.divi:
            result = f'{float(self.first_number)/float(second_number)}'
        elif self.operand == 'Pow':
            result = f'{pow(float(self.first_number),float(second_number))}'
        elif self.operand == self.sqrr:
            result = f'{sqrt(float(self.first_number))}'
        elif self.operand == '1/x':
            result = f'{1/float(self.first_number)}'
        elif self.operand == self.perc:
            result = f'{float(self.first_number)*(float(second_number)/100)}'
        if ceil(float(result)) == floor(float(result)):
            result = ceil(float(result))
        self.entry.insert(0, result)
        self.history_insert(f'=\n{result}\n------\n')
        self.entry.clipboard_append(self.entry.get())
        self.entry.select_range(0, END)



cal = Calculator()