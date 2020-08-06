"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""
from uuid import uuid4
import hashlib

salt = uuid4().hex

memory = {}
while True:

    def kesh_url(some_url):
        hash_object = hashlib.sha3_256(salt.encode() + some_url.encode()).hexdigest()
        res = memory.get(some_url)
        if res is None:
            memory[some_url] = hash_object
        else:
            print(f'{some_url} - есть в кеше.')


    url = input('URL: ')

    kesh_url(url)

    print(memory)
