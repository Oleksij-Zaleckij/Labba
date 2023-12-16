import tkinter as tk
from math import sqrt, sin, cos, radians

def цифра(цифра):
    текст = введення.get()
    введення.delete(0, tk.END)
    введення.insert(tk.END, текст + str(цифра))

def вивести_оператор(оператор):
    текст = введення.get()
    введення.delete(0, tk.END)
    введення.insert(tk.END, текст + оператор)

def обчислити():
    try:
        вираз = введення.get()
        результат = str(eval(вираз))
        введення.delete(0, tk.END)
        введення.insert(tk.END, результат)
    except Exception as e:
        введення.delete(0, tk.END)
        введення.insert(tk.END, "Помилка")

def очистити():
    введення.delete(0, tk.END)

def корінь():
    try:
        число = float(введення.get())
        результат = sqrt(число)
        введення.delete(0, tk.END)
        введення.insert(tk.END, результат)
    except Exception as e:
        введення.delete(0, tk.END)
        введення.insert(tk.END, "Помилка")

def обчислити_sin():
    try:
        кут = float(введення.get())
        результат = sin(radians(кут))
        введення.delete(0, tk.END)
        введення.insert(tk.END, результат)
    except Exception as e:
        введення.delete(0, tk.END)
        введення.insert(tk.END, "Помилка")

def обчислити_cos():
    try:
        кут = float(введення.get())
        результат = cos(radians(кут))
        введення.delete(0, tk.END)
        введення.insert(tk.END, результат)
    except Exception as e:
        введення.delete(0, tk.END)
        введення.insert(tk.END, "Помилка")

root = tk.Tk()
root.title("Інженерний калькулятор")

#поле введення 
введення = tk.Entry(root, width=20, font=('Arial', 16), justify='right')
введення.grid(row=0, column=0, columnspan=4)

#кнопки
ряд1 = ['7', '8', '9', '/']
ряд2 = ['4', '5', '6', '*']
ряд3 = ['1', '2', '3', '-']
ряд4 = ['0', '.', '=', '+']
ряд5 = ['sin', 'cos', '√', 'C']

ряди = [ряд1, ряд2, ряд3, ряд4, ряд5]

for індекс_ряду, ряд in enumerate(ряди):
    for індекс_кнопки, текст_кнопки in enumerate(ряд):
        tk.Button(root, text=текст_кнопки, command=lambda txt=текст_кнопки: обробити_натискання(txt), height=2, width=6).grid(row=індекс_ряду + 1, column=індекс_кнопки)

def обробити_натискання(текст):
    if текст.isdigit() or текст == '.':
        цифра(текст)
    elif текст in ['+', '-', '*', '/']:
        вивести_оператор(текст)
    elif текст == '=':
        обчислити()
    elif текст == 'C':
        очистити()
    elif текст == '√':
        корінь()
    elif текст == 'sin':
        обчислити_sin()
    elif текст == 'cos':
        обчислити_cos()
root.mainloop()


