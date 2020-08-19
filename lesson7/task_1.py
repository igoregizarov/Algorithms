"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. Обязательно доработайте алгоритм (сделайте его умнее).

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение
Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию
"""
from random import randint
from time import process_time
from memory_profiler import memory_usage

lst = [randint(-100, 100) for _ in range(10)]


def my_time_dec(function_to_decorate):
    def around_func():
        t1 = process_time()
        m1 = memory_usage()
        function_to_decorate(lst)
        t2 = process_time()
        m2 = memory_usage()
        print(f'Время работы кода - {t2 - t1}\nВыделено памяти - {m2[0] - m1[0]}')

    return around_func


@my_time_dec
def bubble_sort_better(lst_obj):
    n = 1
    while n < len(lst_obj):
        new_lst = lst_obj.copy()
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        if lst_obj == new_lst:
            break

        n += 1
    return print(lst_obj)


@my_time_dec
def bubble_sort_origin(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]

        n += 1
    return print(lst_obj)


print(f'Массив для сортировки - {lst}')
print('Замер улучшенного кода: ')
bubble_sort_better()
print('Замер оригинального кода: ')
bubble_sort_origin()
"""
В улучшенном коде выделяется память на копию списка для проверки соответствия,
нет эффективности, но есть прирост потребления памяти
"""