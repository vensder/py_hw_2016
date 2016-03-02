#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  2016_python.py
#  
#  Student Dmitry Makarov <vensder@gmail.com>

'''
3.1. Сделать измененную версию задания №2 (п.4 и п.5) - 
  - использовать те типы данных в задании, которые удобно.
  Что для чего пригодилось?
'''

students = [u'Иванов Иван',
            u'Иванов Станислав',
            u'Петров Иван',
            u'Иванов Петр',
            u'Петров Петр',
            u'Сидоров Петр',
            u'Сидоров Иван',]

# 4. Находим количество студентов, в именах которых есть буква "р".
splitted = [students[i].split() for i in range(len(students))]
j = 0
for i in range(len(splitted)):
        if 'р' in splitted[i][1]:
            j += 1
print(u'Количество студентов с буквой "р" в имени: ' + str(j) + u' штуки.\n')


# 5. Находим группы студентов с одинаковыми именами и создаем списки этих групп.

# Создаем словарь из списка студентов. Ключ - множество с последним в цикле именем.
# {name1:{surname1, surname2}, name2:{surname3}...}
#groups_by_names = {students[i].split()[1]:{students[i].split()[0]} for i in range(len(students))}
groups_by_names = {splitted[i][1]:{splitted[i][0]} for i in range(len(students))}

# Добавляем в множество значений каждого имени фамилию, если имя совпадает с ключем
for i in range(len(students)):
    for j in groups_by_names:
        if j == splitted[i][1]:
            groups_by_names[j].add(splitted[i][0])

print(u'Печатаем имя и соответсвующие ему фамилии студентов:\n')
for j in groups_by_names:
    print(j + ':')
    print(str(groups_by_names.get(j)) + '\n')
