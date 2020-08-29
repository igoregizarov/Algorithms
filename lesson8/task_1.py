"""
Задание 1.
Реализуйте кодирование строки "по Хаффману".
У вас два пути:
1) тема идет тяжело? тогда вы можете, опираясь на пример с урока, сделать свою версию алгоритма
Разрешается и приветствуется изменение имен переменных, выбор других коллекций, различные изменения
и оптимизации.
КОПИПАСТ ПРИМЕРА ПРИНИМАТЬСЯ НЕ БУДЕТ!
2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например, через ООП или предложить иной подход к решению.

ВНИМАНИЕ: примеры заданий будут размещены в последний день сдачи.
Но постарайтесь обойтись без них.
"""
from collections import deque


def haff_tree(s):
    d = {}
    for i in s:
        d.update({i: s.count(i)})
    sort_el = deque(sorted(d.items(), key=lambda item: item[1]))
    if len(sort_el) != 1:
        while len(sort_el) > 1:
            w = sort_el[0][1] + sort_el[1][1]
            combo = {0: sort_el.popleft()[0],
                    1: sort_el.popleft()[0]}
            for i, _count in enumerate(sort_el):
                if w > _count[1]:
                    continue
                else:
                    sort_el.insert(i, (combo, w))
                    break
            else:
                sort_el.append((combo, w))

    else:
        w = sort_el[0][1]
        combo = {0: sort_el.popleft()[0], 1: None}
        sort_el.append((combo, w))

    return sort_el[0][0]


code_d = dict()


def haff_codin(tree, path=''):
    if not isinstance(tree, dict):
        code_d[tree] = path
    else:
        haff_codin(tree[0], path=f'{path}0')
        haff_codin(tree[1], path=f'{path}1')


string_code = "beep boop beer!"

haff_codin(haff_tree(string_code))

for i in string_code:
    print(code_d[i], end=' ')



