"""
Задание 6.
Задание на закрепление навыков работы со стеком

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим стеком порогового значения.
Реализуйте по аналогии с примером, рассмотренным на уроке, необходимые методы,
для реализации это структуры, добавьте новые методы (не рассмотренные в примере с урока)
для реализации этой задачи.

После реализации структуры, проверьте ее работу на различных сценариях
"""


class StackClass:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return self.elements == []

    def push_in(self, el):
        if len(self.elements) < 3:
            self.elements.append(el)

    def pop_out(self):
        return self.elements.pop()

    def get_val(self):
        return self.elements[len(self.elements) - 1]

    def stack_size(self):
        return len(self.elements)

    def max_size(self, el):
        if len(self.elements) > 3:
            New_StackClass.push_in(self, el)


class New_StackClass(StackClass):
    def __init__(self):
        super().__init__()


SC_OBJ = StackClass()
print(SC_OBJ.is_empty())
SC_OBJ_NEW = New_StackClass()
SC_OBJ.push_in(1)
SC_OBJ.push_in(33)
SC_OBJ.push_in(11)
SC_OBJ.push_in(3)
SC_OBJ.push_in(1)
SC_OBJ.push_in(33)
SC_OBJ.push_in(11)
SC_OBJ.push_in(3)
print(SC_OBJ.is_empty())
print(SC_OBJ.stack_size())

print(SC_OBJ_NEW.stack_size())
