"""
Задание 1.

Докажите, что словари обрабатываются быстрее, чем списки.

Реализуйте две функции, в первой нужно заполнить элементами список, во второй-словарь
Сделайте замеры времени выполнения каждой из функций

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""

import time

obj_list = [i for i in range(1, 10000000)]

obj_dict = {x: x for x in range(1, 10000000)}


def my_first_decorator(function_to_decorate):

    def around_the_original_function():
        start_time = time.time()
        function_to_decorate()  # Сама функция
        end_time = time.time()
        print(end_time - start_time)

    return around_the_original_function


@my_first_decorator
def obj_list_function():
    obj_list.remove(1000000)


obj_list_function()


@my_first_decorator
def obj_dict_function():
    obj_dict.pop(1000000)


obj_dict_function()