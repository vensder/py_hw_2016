#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
2. Сохранить объект в файл можно так:
    »> import pickle
    »> data = {
    ... 'a': [1, 2.0, 3, 4+6j],
    ... 'b': ("character string", b"byte string"),
    ... 'c': {None, True, False}
    ... }
    »>
    »> with open('data.pickle', 'wb') as f:
    ... pickle.dump(data, f)

    Тогда так его можно прочитать:

    »> with open('data.pickle', 'rb') as f:
    ... data_new = pickle.load(f)

    Сделайте простую базу данных.
    При первом запуске программы она создает файл pickle с данными. 
    При последующих открывает этот файл и выводит на экран содержимое

    3.* Реализовать поиск/фильтрацию в базе данных - то есть вывод по условию.
'''
data = {
        'кот': {'ловит мышей','умеет мяукать'},
        'кит': {'живет в океане','ест планктон'},
        'студент': {'ходит на лекции'},
        'профессор': {'ходит на лекции'},
        }

import pickle
# Пробуем открыть файл с данными. Если его нет, создаем файл с данными.
# Если он есть, но не читается, пишем, что плохой формат.
data_new = ''
try:
    with open('data.p','rb') as f:
        try:
            data_new = pickle.load(f)
        except:
            print('Bad format of file. Remove it?')
            remove = input('yes/no?')
            if remove == 'yes':
                import os
                os.remove('data.p')
        if data_new:
            print(data_new)
except FileNotFoundError:
    with open('data.p','wb') as f:
        pickle.dump(data,f)

# Поиск по ключу
print('Хотите узнать, что делают:')
for i in data.keys():
    print(i)
print('?')
print('Введите кого-нибудь:')
data_object = input()

# Выдача информации об объекте по ключу
if data_object in data.keys():
    print(data_object + ':')
    print(data.get(data_object))
else:
    print('про ' + data_object + ' ничего не знаем')

# Поиск по значению

print('\nЗнаете, кто: ')
for i in data.values():
    print(i)
print('?')

print('Введите вопрос, например:') 
print('Кто ест планктон?')
question = input()

#Кто ходит на лекции?

found = False
for subj, actions in data.items():
    for action in actions:
        if action in question:
            print(subj)
            found = True

for subj in data.keys():
    for action in data.get(subj):
        if action in question:
            print(subj)
            found = True

if not found:
    print('Извините, но мы не знаем, ' + question.lower())



