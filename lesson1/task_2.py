"""
Задание 2.

Реализуйте два алгоритма.

Первый, в виде функции, должен обеспечивать поиск минимального значения для списка.
В основе алгоритма должно быть сравнение каждого числа со всеми другими элементами списка.
Сложность такого алгоритма: O(n^2) - квадратичная.

Второй, в виде функции, должен обеспечивать поиск минимального значения для списка.
Сложность такого алгоритма: O(n) - линейная.

Примечание:
Построить список можно через генератор списка.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.
"""
import random

list_obj = [i for i in range(1, random.randint(2, 20))]
random.shuffle(list_obj)

# list_obj = [i for i in range(2, 10)]
print(list_obj)


def check_1(list_obj):  # O(n^2)
    minimal = list_obj[0]
    for i in list_obj:
        for j in list_obj:
            if i < minimal:
                if i < j:
                    minimal = i

    print(minimal)


def check_2(list_obj):  # O(n)
    minimal = list_obj[0]
    for i in range(1, len(list_obj)):
        if list_obj[i] < minimal:
            minimal = list_obj[i]
    print(minimal)


def check_2_1(list_obj):  # O(n)
    print(min(list_obj))


check_1(list_obj)

check_2(list_obj)

check_2_1(list_obj)
