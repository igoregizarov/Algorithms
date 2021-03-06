"""
1.	Написать программу, которая будет складывать, вычитать, умножать или делить
два числа. Числа и знак операции вводятся пользователем. После выполнения
вычисления программа не должна завершаться, а должна запрашивать новые данные
для вычислений. Завершение программы должно выполняться при вводе символа '0'
в качестве знака операции. Если пользователь вводит неверный знак
(не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и
снова запрашивать знак операции.

Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.

Подсказка:
Вариант исполнения:
- условие рекурсивного вызова - введена операция +, -, *, /
- условие завершения рекурсии - введена операция 0

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7

Пример:
Введите операцию (+, -, *, / или 0 для выхода): +
Введите первое число: 214
Введите второе число: 234
Ваш результат 448
Введите операцию (+, -, *, / или 0 для выхода): -
Введите первое число: вп
Вы вместо трехзначного числа ввели строку (((. Исправьтесь
Введите операцию (+, -, *, / или 0 для выхода):
"""


def calc():
    res = None
    operator = input("Введите операцию (+, -, *, / или 0 для выхода)\n")
    if operator == '0':
        return print("Выход")
    elif operator in ['+', '-', '*', '/']:
        try:
            var_1 = int(input('Введите первое число: '))
            var_2 = int(input('Введите второе число: '))
            if operator == '+':
                res = var_1 + var_2

            elif operator == '-':
                res = var_1 - var_2

            elif operator == '*':
                res = var_1 * var_2

            elif var_2 == 0 and operator == '/':
                print('Деление на ноль!')

            elif operator == '/':
                res = var_1 / var_2

        except ValueError:
            print('Введено не число.')

    else:
        print('Ошибка ввода.')

    if res != None:
        print(f'Результат = {res}')
    calc()


calc()
