"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""
from timeit import Timer, timeit, repeat, default_timer

array = [1, 3, 1, 3, 4, 5, 1]


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def func_3():
    n = [(array.count(i)) for i in array]
    return f'Чаще всего встречается число {array.index(max(n))}, ' \
           f'оно появилось в массиве {(max(n))} раз(а)'


print(func_1())
print(func_2())
print(func_3())

t1 = Timer("func_1()", "from __main__ import func_1")
print(t1.timeit(number=10000))

t2 = Timer("func_2()", "from __main__ import func_2")
print(t1.timeit(number=10000))

t3 = Timer("func_3()", "from __main__ import func_3")
print(t1.timeit(number=10000))


"""
Улучшить алгоритм не получилось.
"""