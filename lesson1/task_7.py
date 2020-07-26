"""
Задание 5.
Задание на закрепление навыков работы с деком

В рассмотренном на уроке листинге есть один недостаток
Приведенный код способен "обработать" только строку без пробелов, например, 'топот'

Но могут быть и такие палиндромы, как 'молоко делили ледоколом'

Вам нужно доработать программу так, чтобы она могла выполнить проверку на палиндром
и в таких строках (включающих пробелы)
"""


class DequeClass:
    def __init__(self):
        self.elments = []

    def is_empty(self):
        return self.elements == []

    def add_to_front(self, elements):
        self.elements.append(elements)

    def add_to_rear(self, elements):
        self.elements.insert(0, elements)

    def remove_from_front(self):
        return self.elments.pop()

    def remove_from_rear(self):
        return self.elments.pop(0)

    def size(self):
        return len(self.elements)
