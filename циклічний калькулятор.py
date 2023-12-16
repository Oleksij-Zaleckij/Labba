while True:
    print("Оберіть операцію:")
    print("1. Додавання")
    print("2. Віднімання")
    print("3. Множення")
    print("4. Ділення")
    print("5. Вихід")

    робимо = input("Введіть номер операції (1/2/3/4/5): ")

    if робимо == '5':
        print("До побачення!")
        break

    try:
        a = float(input("Введіть перше число: "))
        b = float(input("Введіть друге число: "))
    except ValueError:
        print("Неправильний ввід чисел")
        continue

    if робимо in ('1', '2', '3', '4'):
        if робимо == '1':
            t = a + b
        elif робимо == '2':
            t = a - b
        elif робимо == '3':
            t = a * b
        elif робимо == '4':
            if b != 0:
                t = a / b
            else:
                print("Ділення на нуль неможливе")
                continue

        print(f"Результат: {t}")

    else:
        print("Неправильний вибір операції")
