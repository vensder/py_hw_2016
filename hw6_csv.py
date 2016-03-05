#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  2016_python.py
#  
#  Student Dmitry Makarov <vensder@gmail.com>

#import pickle
import csv

# Базовый словарь англ. языка, на случай, если нет файла
# Имеет структуру словаря, значения в котором - множества(sets) переводов.
en_ru_base = {
            u'key': {u'ключ',u'клавиша',u'код',},
            u'space': {u'пространство',u'космос',u'пробел',},
            u'escape': {u'побег',u'выход',u'спасение',},
            u'shift': {u'сдвиг',u'изменение',u'переключение'},
}

en_ru_new = {} # пустой словарь, куда загрузим файл, если он есть

try: # Пробуем открыть файл
    with open('dict.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            en_ru_new[row['key']] = eval(row['value']) # eval преобразует строку str типа '{1,2,3}' в set {1,2,3}
except FileNotFoundError: # если файл не найден, скидываем в него наш словарь
    with open('dict.csv','w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['key','value']) # пользуемся классом DictWriter, задаем поля
        writer.writeheader() # пишем названия полей
        for key in en_ru_base.keys(): # заполняем ключами и значениями (value = str(set))
            writer.writerow({'key': key, 'value': en_ru_base.get(key)})
        en_ru_new = en_ru_base # присваеваем содержимое базового рабочему

# Функция запроса продолжения/прекращения общения
def choice():
    choice = input(u'Да: Enter, 1, Y, y / Нет - любая другая клавиша\n')
    choice = choice.lower()
    yes = [u'', u'да', u'', u'1', u'y', u'yes']

    if choice in yes:
        choice = u'yes'
    else:
        choice = u'no'
    return choice

# Функция интерактивного общения со словарем
def interact():
    # Поиск по ключу
    print(u'Чтобы узнать перевод слов:')
    for k in en_ru_new.keys():
        print(u'\t',k)
    print(u'введите любое из них:')
    eng_word = input()

    # Выдача перевода по ключу
    if eng_word in en_ru_new.keys():
        print(eng_word + ':', (', '.join(en_ru_new.get(eng_word))))
    else:
        print(u'Слова', eng_word, u'нет в словаре')

    print(u"Хотите узнать перевод другого слова?")
    if choice() == u"yes":
        interact()
    else:
        print(u"Bye")
        quit()

interact()
