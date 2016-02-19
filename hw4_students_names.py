#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#4

#4.1. задание по студентам - через lambda


students = ['Иванов Иван',
            'Иванов Станислав',
            'Петров Иван',
            'Иванов Петр',
            'Петров Петр',
            'Сидоров Петр',
            'Сидоров Иван',]

# 4.1 Находим количество студентов, в именах которых есть буква "р".

# Разбиваем список на подсписки с фамилиями и именами
l_split = lambda lst: [i.split() for i in lst]
students_splitted = l_split(students)

# Получаем список только из имен:
l_names = lambda lst: [lst[i][1] for i in range(len((lst)))]
students_names = l_names(students_splitted)

# Получаем список только из имен, содержащих букву "р"
l_names_r = lambda lst: [ lst[i]  for i in range(len(lst)) if 'р' in lst[i] ]
students_names_r = l_names_r(students_names)

# Количество студентов с буквой "р" в имени - это длина полученного списка:
print(len(students_names_r))




#4.2. задание по БД - через def
