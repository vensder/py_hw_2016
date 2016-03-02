#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  2016_python.py
#  
#  Student Dmitry Makarov <vensder@gmail.com>

# module students

students = [u'Иванов Иван',
            u'Иванов Станислав',
            u'Петров Иван',
            u'Иванов Петр',
            u'Петров Петр',
            u'Сидоров Петр',
            u'Сидоров Иван',]

quantity = len(students)

def print_students():
    print(u'\nСписок студентов:')
    for i in range(quantity):
        print(str(i+1)+'.',students[i])
