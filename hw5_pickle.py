#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  2016_python.py
#  
#  Student Dmitry Makarov <vensder@gmail.com>

#5.3. в задании с pickle тоже try-except
import pickle

# Базовый словарь, на случай, если нет файла
en_ru_dump = {
        u'key': {u'ключ',u'клавиша',u'код',},
        u'space': {u'пространство',u'космос',u'пробел',},
        u'escape': {u'побег',u'выход',u'спасение'},
        u'shift': {u'сдвиг',u'изменение',u'переключение'},
        }

en_ru_new = None

# Загрузка словаря из файла
try:
    with open('en_ru.p','rb') as f:
        en_ru_new = pickle.load(f)
# Если файл не найден, создаем его, сбрасывая базовый словарь
except FileNotFoundError:
    with open('en_ru.p','wb') as f:
        pickle.dump(en_ru_dump,f)
        en_ru_new = en_ru_dump # присваеваем содержимое базового рабочему

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
