#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  2016_python.py
#  
#  Student Dmitry Makarov <vensder@gmail.com>

#1.5
students = [
        'Ivanov Ivan',
        'Ivanov Stanislav',
        'Petrov Ivan',
        'Ivanov Petr',
        'Petrov Petr',
        'Sidorov Petr',
        'Sidorov Ivan',]

# Split each element of list to list whith Surname, Name
for i in range(len(students)):
    students[i] = students[i].split(' ')

# Create/truncate file with name 'group_Name'
for i in range(len(students)):
    f = open('group_' + students[i][1],'w')
    f.close()

# Append Surname to file 'group_Name'
for i in range(len(students)):
    f = open('group_' + students[i][1],'a')
    f.write(students[i][0] + '\n')
    f.close()

list0 = []
# get list with uniq names, insert empty list after each name
for i in range(len(students)):
    if not students[i][1] in list0:
        list0.append(students[i][1])
        list0.append([])
print(list0)

# insert in each empty nested list surname after name
for i in range(1,len(list0),2):
    for j in range(len(students)):
        if students[j][1] == list0[i-1] and not students[j][0] in list0[i]:
            list0[i].append(students[j][0])

for i in range(len(list0)):
    print(list0[i])



