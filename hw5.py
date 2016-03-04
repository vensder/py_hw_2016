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
# 3. в задании с pickle тоже try-except # см. второй файл.

#1
import students

students.print_students()
#print(students.quantity)

#2
def input_number():
    print(
    u'''Введите порядковый номер студента.
    Номер должен быть от 1 до''', students.quantity)
    try:
        index = int(input()) - 1
        print(u'\nВы ввели номер:', index+1)
        return index
    except ValueError:
        print(u'Ввели какую-то фигню')
        quit()

def try_output_student(index):
    try:
        print(u'\nСтудент под номером ' + str(index+1) + ':', students.students[index])
        return True
    except IndexError:
        print(u'Порядковый номер за пределами диапазона, извините...')
        input_number()
        return False

index = input_number()
while not try_output_student(index):
    index = input_number()


#3
print(u'\nВведите диапазон номеров студентов в формате "x-y", где x - начало, а y - конец диапазона')

students_range = input().split('-')

try:
    begin = int(students_range[0])
except ValueError:
    print(u'Ввели неправильное значение начала диапазона')
    quit()

try:
    end = int(students_range[1])
except ValueError:
    print(u'Ввели неправильное значение конца диапазона')
    quit()

print(u'\nДиапазон студентов(срез):')
print(students.students[begin-1:end])

#4
i=0
for s in students.students:
    if s.find('р') != -1:
        i+=1

input(u'Нажмите Enter для продолжения')

print(u'\nКоличество студентов с буквой "р":', i)

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
print(u'\nГруппы студентов по именам:')
for i in range(len(list0)):
    print(list0[i])


