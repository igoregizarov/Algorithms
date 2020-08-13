"""
2.	Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections
Также попробуйте решить задачу вообще без collections и применить только ваши знания по ООП
(в частности по перегрузке методов)
"""
from collections import deque

n1 = deque(list(input('Введите шестнадцатеричное число 1: ')))
n2 = deque(list(input('Введите шестнадцатеричное число 2: ')))
print(f"Первое число - {n1}")
print(f"Второе число - {n2}")
dict_obj = {'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}


def hex_calc(numb):
    list_obj = deque()
    for i in range(len(numb)):
        if numb[i].isdigit() == True:
            list_obj.append(int(numb[i]) * (16 ** (len(numb) - (i + 1))))
        else:
            list_obj.append(dict_obj.get(numb[i]) * (16 ** (len(numb) - (i + 1))))
    return list_obj


summ = deque(hex(sum(hex_calc(n1) + hex_calc(n2))))

summ.popleft()
summ.popleft()

mull = deque(hex(sum(hex_calc(n1)) * sum(hex_calc(n2))))

mull.popleft()
mull.popleft()

print(f"Сумма чисел из примера: {summ}, произведение - {mull}.")
