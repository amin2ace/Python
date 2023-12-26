import customtkinter as t
from customtkinter import END
from typing import Callable
from math import sqrt, pow, ceil, floor


class Calculator:
    def __init__(self):
        root = t.CTk()
        get_window_geo: tuple[int] = root.winfo_screenwidth(), root.winfo_screenheight()
        root.width: int = 315
        root.height: int = 360
        geometry: str = f"{root.width}x{root.height}+{get_window_geo[0]//2 - root.width//2}+{get_window_geo[1]//2 - root.height//2}"
        root.geometry(geometry)
        root.resizable(False, False)

        ### Fonts
        btns_font = t.CTkFont(family='centry', weight='bold', size=14)
        ent_font = t.CTkFont(family='calibri', size=16)
        his_font = t.CTkFont(family='centry', size=8)

        ### Entry Pane
        self.ent_pane = t.CTkFrame(root, width=100)
        self.entry = t.CTkEntry(self.ent_pane, width=200, height=50, border_width=2, font=ent_font)
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
        self.btn_pane = t.CTkFrame(root, width=100)
        self.btn_pane.grid(column=0, row=1)
        self.btns: list[t.CTkButton] = []
        col, ro = 0, 0
        for _, btn in enumerate(btn_list):
            self.btns.append(t.CTkButton(self.btn_pane, text=btn, font=btns_font, border_width=2, width=50, height=50,
                                      command=lambda x=btn: self.get_btns(x)).grid(column=col, row=ro))
            col += 1
            if col >= 4: col, ro = 0, ro + 1

        
        ### History Pane
        self.his_pane: t.CTkFrame = t.CTkFrame(root, width=50, height=50)
        self.his_frame: t.CTkScrollableFrame = t.CTkScrollableFrame(self.his_pane, label_text='History', width=80, label_font=his_font, height=300)
        self.his_label: t.CTkLabel = t.CTkLabel(self.his_frame, text='', font=his_font, height=350, width=80)
        self.his_pane.grid(column=1, row=0, padx=6, rowspan=2)
        self.his_frame.grid(column=0, row=0, sticky='n')
        self.his_label.grid(column=0, row=0, sticky='ne')


        root.mainloop()

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
        t = ''
        self.his_label.clipboard_append(t+f'{insertion}\n')
        self.his_label.configure(text=self.his_label.clipboard_get())
        t = f'{insertion}\n'
        ...
    def history_clear(self):
        self.his_label.configure(text='')
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