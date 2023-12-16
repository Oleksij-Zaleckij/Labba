import tkinter as tk
from math import sin, cos, radians
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Калькулятор")

        self.entry_var = tk.StringVar()
        self.entry = tk.Entry(master, textvariable=self.entry_var, font=('Arial', 18), bd=5, insertwidth=4, justify='right')
        self.entry.grid(row=0, column=0, columnspan=6, sticky='nsew')

        buttons = [
            '7', '8', '9', '4',
            '5', '6', '1', '2',
            '3', '0', '-', '.',
            '+', '=', '/', '*',
            'sin', 'cos',
            'bin', 'oct', 'hex'  
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            if button == '=':
                tk.Button(master, text=button, padx=20, pady=20, font=('Arial', 14),
                          command=lambda btn=button: self.button_click(btn)).grid(row=row_val, column=col_val, columnspan=2, sticky='nsew')
                col_val += 2
            elif button in ['sin', 'cos']:
                tk.Button(master, text=button, padx=20, pady=20, font=('Arial', 14),
                          command=lambda btn=button: self.button_click(btn)).grid(row=row_val, column=col_val, sticky='nsew')
                col_val += 1
            else:
                tk.Button(master, text=button, padx=20, pady=20, font=('Arial', 14),
                          command=lambda btn=button: self.button_click(btn)).grid(row=row_val, column=col_val, sticky='nsew')
                col_val += 1
            if col_val > 5:
                col_val = 0
                row_val += 1

        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)

        self.number_system = 'decimal' 

    def button_click(self, value):
        current = self.entry_var.get()

        if value == '=':
            try:
                result = self.calculate(current)
                self.entry_var.set(result)
            except Exception:
                self.entry_var.set("Error")
        elif value in ['sin', 'cos']:
            try:
                angle = float(current)
                result = sin(radians(angle)) if value == 'sin' else cos(radians(angle))
                self.entry_var.set(str(result))
            except ValueError:
                self.entry_var.set("Error")
        elif value in ['bin', 'oct', 'hex']:
            self.number_system = value
            self.entry_var.set(f"Switched to {value}")
        else:
            self.entry_var.set(current + value)

    def calculate(self, expression):
        try:
            if self.number_system == 'decimal':
                return str(eval(expression))
            elif self.number_system == 'bin':
                return bin(eval(expression))[2:]
            elif self.number_system == 'oct':
                return oct(eval(expression))[8:]
            elif self.number_system == 'hex':
                return hex(eval(expression))[16:]
        except Exception:
            messagebox.showerror("Error", "Invalid expression")
            return "Error"

root = tk.Tk()
app = CalculatorApp(root)
root.mainloop()

