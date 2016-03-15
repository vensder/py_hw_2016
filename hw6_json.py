#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  2016_python.py
#  
#  Student Dmitry Makarov <vensder@gmail.com>

import json

# Базовый словарь, на случай, если нет файла
en_ru_base = {
        'key': 'ключ',
        'space': 'пространство',
        'escape': 'побег',
        'shift': 'сдвиг',
        }

en_ru_new = None

try: # Загрузка словаря из файла
    js_from_file = json.load(open('jsonfile.json'))
    print(type(js_from_file))
    en_ru_new = json.loads(js_from_file)
    print(type(en_ru_new))
    print(en_ru_new)
except FileNotFoundError: # Если файл не найден, создаем его, сбрасывая базовый словарь
    js = json.dumps(en_ru_base, ensure_ascii=False) # convert dict to json
    json.dump(js, open('jsonfile.json', 'w'), ensure_ascii=False)
    en_ru_new = en_ru_base # присваеваем содержимое базового рабочему
    
def choice():
    '''Функция запроса продолжения/прекращения общения'''
    choice = input(u'Да: Enter, 1, Y, y / Нет - любая другая клавиша\n')
    choice = choice.lower()
    yes = [u'', u'да', u'', u'1', u'y', u'yes']

    if choice in yes:
        choice = u'yes'
    else:
        choice = u'no'
    return choice

def interact():
    '''Функция интерактивного общения со словарем'''
    # Поиск по ключу
    print(u'Чтобы узнать перевод слов:')
    for k in en_ru_new.keys():
        print(u'\t',k)
    print(u'введите любое из них:')
    eng_word = input()

    # Выдача перевода по ключу
    if eng_word in en_ru_new.keys():
        print(eng_word + ':', (en_ru_new.get(eng_word)))
    else:
        print(u'Слова', eng_word, u'нет в словаре')

    print(u"Хотите узнать перевод другого слова?")
    if choice() == u"yes":
        interact()
    else:
        print(u"Bye")
        quit()

interact()
