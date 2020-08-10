"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""
import cProfile
from timeit import Timer, timeit, repeat, default_timer


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


t1 = Timer("revers(enter_num=123456789)", "from __main__ import revers")
print(t1.timeit(number=10000))

t2 = Timer("revers2(enter_num=123456789)", "from __main__ import revers2")
print(t1.timeit(number=10000))

t3 = Timer("revers3(enter_num=123456789)", "from __main__ import revers3")
print(t1.timeit(number=10000))


cProfile.run('revers(enter_num=123456789, revers_num=0)')
cProfile.run('revers_2(enter_num=123456789, revers_num=0)')
cProfile.run('revers_3(enter_num=123456789)')


"""
Быстрее третья функция так как используется встроенный способ реверса на месте.
Он и является самым оптимальным.
"""