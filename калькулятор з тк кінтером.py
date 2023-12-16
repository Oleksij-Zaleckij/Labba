import tkinter as tk

def obrobiti_click(що):
    try:
        a = float(entry_num1.get())
        b = float(entry_num2.get())

        if що == 'Додавання':
            result = a + b
        elif що == 'Віднімання':
            result = a - b
        elif що == 'Множення':
            result = a * b
        elif що == 'Ділення':
            if b != 0:
                result = a / b
            else:
                result = "Ділення на нуль неможливе"

        label_result.config(text="Результат: " + str(result))
    except ValueError:
        label_result.config(text="Неправильний ввід чисел")

root = tk.Tk()
root.title("Калькулятор")

entry_num1 = tk.Entry(root, width=10)
entry_num1.grid(row=0, column=0, padx=10, pady=10)

entry_num2 = tk.Entry(root, width=10)
entry_num2.grid(row=0, column=1, padx=10, pady=10)

button_add = tk.Button(root, text='Додавання', command=lambda: obrobiti_click('Додавання'))
button_add.grid(row=1, column=0, pady=5)

button_subtract = tk.Button(root, text='Віднімання', command=lambda: obrobiti_click('Віднімання'))
button_subtract.grid(row=1, column=1, pady=5)

button_multiply = tk.Button(root, text='Множення', command=lambda: obrobiti_click('Множення'))
button_multiply.grid(row=2, column=0, pady=5)

button_divide = tk.Button(root, text='Ділення', command=lambda: obrobiti_click('Ділення'))
button_divide.grid(row=2, column=1, pady=5)

label_result = tk.Label(root, text="Результат: ")
label_result.grid(row=3, columnspan=2, pady=10)

root.mainloop()
