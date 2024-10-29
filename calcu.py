import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import END

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title('Calculator')
        self.create_widgets()
        self.current_value = ''
        
    def create_widgets(self):
        self.display = ttk.Entry(self.master, justify='right', font=('Arial',20))
        self.display.grid(row=0, column=0, columnspan=4, padx=5,pady=5, sticky='nsew')
        
        buttons = [
            'AC', 'DEL', '', '/',
            '7', '8', '9', '*',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            '0', '.', '=', ''
            
        ]
        row = 1
        col = 0
        for button in buttons:
            if button:
                cmd = lambda x=button: self.click(x)
                ttk.Button(self.master, text=button, command=cmd).grid(row=row, column=col, padx=5, pady=5, sticky='nsew')
            col += 1
            if col > 3:
                col = 0 
                row += 1
                
    def click(self, key):
        if key == 'AC':
            self.current_value = ''
            self.display.delete(0, END)
        elif key == 'DEL':
            self.current_value = self.current_value[:-1]
            self.display.delete(0, END)
            self.display.insert(END, self.current_value)
        elif key == '=':
            try:
                result = eval(self.current_value)
                self.display.delete(0, END)
                self.display.insert(END, str(result))
                self.current_value = str(result)
                
            except:
                    self.display.delete(0, END)
                    self.display.insert(END, 'Error')
                    self.current_value = ''
        else:
                self.current_value += key
                self.display.delete(0, END)
                self.display.insert(END, self.current_value) 
                
if __name__ == '__main__':
    root = ttk.Window(themename='darkly')
    app = Calculator(root)
    root.mainloop()
                
                                   