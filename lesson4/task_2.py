"""
Задание 2.

Приведен код, который формирует из введенного числа
обратное по порядку входящих в него цифр.
Задача решена через рекурсию

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Подсказка: примените мемоизацию

Добавьте аналитику: что вы сделали и почему
"""

from timeit import Timer, timeit, repeat, default_timer

number = 123456


def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


t1 = Timer("recursive_reverse(number)", "from __main__ import recursive_reverse, number")
print(t1.timeit(number=10000))

print(recursive_reverse(123456))


def recursive_reverse(number):
    if number == 1:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


t1 = Timer("recursive_reverse(number=123)", "from __main__ import recursive_reverse")
print(t1.timeit(number=10000))

print(recursive_reverse(123456))


"""
Скорректировал код на верную работу, глубина рекурсии уменьшилась, код стал выполняться быстрей.
Как сделать с мемоизацией не разобрался.
"""