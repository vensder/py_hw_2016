#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  2016_python.py
#  
#  Student Dmitry Makarov <vensder@gmail.com>

language = input('Choise the language: type "en" for English or type "ru" for Russian:\n')

#1
if language == 'ru':
    students = ['Иванов Иван',
                'Иванов Станислав',
                'Петров Иван',
                'Иванов Петр',
                'Петров Петр',
                'Сидоров Петр',
                'Сидоров Иван',]
else:
    students = ['Ivanov Ivan',
                'Ivanov Stanislav',
                'Petrov Ivan',
                'Ivanov Petr',
                'Petrov Petr',
                'Sidorov Petr',
                'Sidorov Ivan',]

quantity = len(students)

if language == 'ru':
    print('\nСписок студентов:')
else:
    print('\nStudents list:')
for i in range(quantity):
    print(str(i+1)+'.',students[i])

#2
if language == 'ru':
    print(
'''Введите порядковый номер студента.
Номер должен быть от 1 до''', quantity)
else:
    print('''
Input the student number, please
The number should be from 1 to''', quantity)
index = int(input()) - 1

if not (0 <= index < quantity):
    if language == 'ru':
        print('Порядковый номер за пределами диапазона, извините...')
    else:
         print('Index out of range, sorry...')
    quit()

if language == 'ru':
    print('\nВы ввели номер:', index+1)
    print('\nСтудент под номером ' + str(index+1) + ':', students[index])
else:
    print('\nYour number is:', index+1)
    print('\nStudent with number', index+1, 'is', students[index])

#3
if language == 'ru':
    print('\nВведите диапазон номеров студентов в формате "x-y", где x - начало, а y - конец диапазона')
else:
    print('\nInput range of students numbers in format "x-y", where x is begin, y is end of range:')

students_range = input().split('-')
begin = int(students_range[0])
end = int(students_range[1])

if language == 'ru':
    print('\nДиапазон студентов(срез):')
else:
    print('\nRange of students(slice):')
print(students[begin-1:end])

#4
i=0
if language == 'ru':
    for s in students:
        if s.find('р') != -1:
            i+=1
else:
    for s in students:
        if s.find('r') != -1:
            i+=1

if language == 'ru':
    print('\nКоличество студентов с буквой "р":', i)
else:
    print('\nQuantity of students with letter "r" is:', i)

#5
# Split each element of list to list whith Surname, Name
for i in range(len(students)):
    students[i] = students[i].split(' ')

# Way # 1
# Create/truncate file with name 'group_Name'
for i in range(len(students)):
    f = open('group_' + students[i][1],'w')
    f.close()

# Append Surname to file 'group_Name'
for i in range(len(students)):
    f = open('group_' + students[i][1],'a')
    f.write(students[i][0] + '\n')
    f.close()

# Way # 2
list0 = []
# get list with uniq names, insert empty list after each name
for i in range(len(students)):
    if not students[i][1] in list0:
        list0.append(students[i][1])
        list0.append([])
#print(list0)

# insert in each empty nested list surname after name
for i in range(1,len(list0),2):
    for j in range(len(students)):
        if students[j][1] == list0[i-1] and not students[j][0] in list0[i]:
            list0[i].append(students[j][0])

#print name and surnames
if language == 'ru':
    print('\nГруппы студентов по именам:')
else:
    print('\nGroups of students by their names:')
for i in range(len(list0)):
    print(list0[i])
