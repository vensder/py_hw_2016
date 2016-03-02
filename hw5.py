#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  2016_python.py
#  
#  Student Dmitry Makarov <vensder@gmail.com>

# 5

# 1. задание со студентами делим на несколько
# модулей с функциями + main.py

# 2. срезы и индексы с использованием try-except

# 3. в задании с pickle тоже try-except

#1

import students

students.print_students()
#print(students.quantity)

#2
print(
'''Введите порядковый номер студента.
Номер должен быть от 1 до''', students.quantity)

index = int(input()) - 1

if not (0 <= index < students.quantity):
    print('Порядковый номер за пределами диапазона, извините...')
    quit()

print('\nВы ввели номер:', index+1)
print('\nСтудент под номером ' + str(index+1) + ':', students.students[index])

#3
print('\nВведите диапазон номеров студентов в формате "x-y", где x - начало, а y - конец диапазона')

students_range = input().split('-')
begin = int(students_range[0])
end = int(students_range[1])

print('\nДиапазон студентов(срез):')
print(students.students[begin-1:end])

#4
i=0
for s in students.students:
    if s.find('р') != -1:
        i+=1

input('Нажмите Enter для продолжения')

print('\nКоличество студентов с буквой "р":', i)

#5
# Split each element of list to list whith Surname, Name
for i in range(len(students.students)):
    students.students[i] = students.students[i].split(' ')

list0 = []
# get list with uniq names, insert empty list after each name
for i in range(len(students.students)):
    if not students.students[i][1] in list0:
        list0.append(students.students[i][1])
        list0.append([])
#print(list0)

# insert in each empty nested list surname after name
for i in range(1,len(list0),2):
    for j in range(len(students.students)):
        if students.students[j][1] == list0[i-1] and not students.students[j][0] in list0[i]:
            list0[i].append(students.students[j][0])

#print name and surnames
print('\nГруппы студентов по именам:')
for i in range(len(list0)):
    print(list0[i])


