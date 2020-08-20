"""
Задание 1.
Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Можно взять задачи с курса Основ или с текущего курса Алгоритмов

Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""
from memory_profiler import profile
from memory_profiler import memory_usage
import time
from pympler import asizeof


@profile
def hex_my(numb='c4f'):
    dict_obj = {'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}
    list_obj = []
    for i in range(len(numb)):
        if numb[i].isdigit() == True:
            list_obj.append(int(numb[i]) * (16 ** (len(numb) - (i + 1))))
        else:
            list_obj.append(dict_obj.get(numb[i]) * (16 ** (len(numb) - (i + 1))))
    return sum(list_obj)


t1 = time.process_time()
m1 = memory_usage()
print(f"Число - {hex_my('c4f')}")
t2 = time.process_time()
m2 = memory_usage()
print(f'Затрачено памяти на мою функцию {m2[0] - m1[0]}')
print(f'Затрачено времени на мою функцию {t2 - t1}')


@profile
def hex_includ(n='c4f'):
    return int(n, 16)


t1 = time.process_time()
m1 = memory_usage()
print(f"Число {hex_includ('c4f')}")
t2 = time.process_time()
m2 = memory_usage()
print(f'Затрачено памяти на встроенную функцию {m2[0] - m1[0]}')
print(f'Затрачено времени на встроенную функцию {t2 - t1}')



"""
Проанализировал написанную мною функцию перевода числа из 16-тиричной системы в 2-ю, сравнил со встроенной функцией "INT"
При разном входном числе в профилировщике MEM Usege не изменяются ни в одной функции.
Но при болле детальном анализе выявлено - встроенная функция "INT" отрабатывает по времени быстрее и потребляет меньше памяти!
"""


class Client_Class:
    def __init__(self, param_x, param_y, param_z):
        self.param_x = 'User_name'
        self.param_y = 'Pass_hash'
        self.param_z = 'Mail'


obj = Client_Class('John', 'hjhgg12342jk', '@mail')
print(obj.param_x)
print(obj.param_y)
print(obj.param_z)
obj.param_z = 'Jhon@mail'
print(obj.param_z)
print(obj.__dict__)
print(f"Занято место обычный словарь - \033[31m{asizeof.asizeof(obj)}\033[0m")


class Client_Class:
    __slots__ = ['param_x', 'param_y', 'param_z']

    def __init__(self, param_x, param_y, param_z):
        self.param_x = 'User_name'
        self.param_y = 'Pass_hash'
        self.param_z = 'Mail'


obj = Client_Class('John', 'hjhgg12342jk', '@mail')
print(obj.param_x)
print(obj.param_y)
print(obj.param_z)
obj.param_z = 'Jhon@mail'
print(obj.param_z)
print(obj.__slots__)
print(f'Занято место используем слоты - \033[31m{asizeof.asizeof(obj)}\033[0m')
print(obj.param_x)
print(obj.param_y)


"""
Очень интересная технология со слотами, действительно экономия памяти в два раза и определенная защита от не желательных изменений.
Реализовал через ООП регистрацию пользователей в системе.
"""