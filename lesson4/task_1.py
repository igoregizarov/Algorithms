"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему
"""
from timeit import Timer, timeit, repeat, default_timer


def func_1(nums=list(range(10))):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums=list(range(10))):
    new_arr = [i for i in nums if i % 2 == 0]
    return new_arr


t = Timer("func_1(nums=list(range(10)))", "from __main__ import func_1")
print(t.timeit(number=10000))

t1 = Timer("func_2(nums=list(range(10)))", "from __main__ import func_2")
print(t1.timeit(number=10000))


"""
Вместо цикле сделал гениратор, так быстрее.
"""
