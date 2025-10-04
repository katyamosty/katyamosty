def calculator():
    print("Простой калькулятор")
    print("Доступные операции: +, -, *, /")
    
    try:
        num1 = float(input("Введите первое число: "))
        operator = input("Введите оператор (+, -, *, /): ")
        num2 = float(input("Введите второе число: "))

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                print("Ошибка: деление на ноль!")
                return
            result = num1 / num2
        else:
            print("Ошибка: неверный оператор!")
            return

        print(f"Результат: {num1} {operator} {num2} = {result}")

    except ValueError:
        print("Ошибка: введите корректное число.")

# Запуск калькулятора
if __name__ == "__main__":
    calculator()
