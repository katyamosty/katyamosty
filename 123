import tkinter as tk

from tkinter import messagebox

def click_button(value):

current = entry.get()

entry.delete(0, tk.END)

entry.insert(0, current + str(value))

def clear():

entry.delete(0, tk.END)

def calculate():

try:

result = eval(entry.get())

entry.delete(0, tk.END)

entry.insert(0, str(result))

except Exception as e:

messagebox.showerror("Ошибка", "Некорректное выражение")

clear()

# Создание окна

root = tk.Tk()

root.title("Калькулятор")

root.geometry("300x400")

# Поле ввода

entry = tk.Entry(root, width=16, font=("Arial", 24), borderwidth=2, relief="solid", justify="right")

entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Кнопки

buttons = [

('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),

('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),

('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),

('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),

('C', 5, 0)

]

for (text, row, col) in buttons:

if text == '=':

btn = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14),

command=calculate)

elif text == 'C':

btn = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14),

command=clear)

else:

btn = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14),

command=lambda t=text: click_button(t))

btn.grid(row=row, column=col, padx=5, pady=5)

# Запуск приложения

root.mainloop()
