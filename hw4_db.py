#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# задание по БД - через def

import pickle

from time import sleep

data = {
        'кот': {'ловит мышей','умеет мяукать'},
        'кит': {'живет в океане','ест планктон'},
        'студент': {'ходит на лекции'},
        'профессор': {'ходит на лекции'},
        }

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
            pass
#            print(data_new)
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

sleep(1)

# Выдача информации об объекте по ключу
if data_object in data.keys():
    print(data_object + ':')
    print(data.get(data_object))
else:
    print('про ' + data_object + ' ничего не знаем')

sleep(2)
# Поиск по значению
print('\nЗнаете, кто: ')
for i in data.values():
    print(i)
print('?')

sleep(1)
print('Введите вопрос, например:') 
print('Кто ест планктон?')
question = input()

sleep(3)
#Кто ходит на лекции?

found = False
for subj in data.keys():
    for action in data.get(subj):
        if action in question:
            print(subj)
            found = True

if not found:
    print('Извините, но мы не знаем, ' + question.lower())

