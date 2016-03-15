#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  2016_python.py
#  
#  Student Dmitry Makarov <vensder@gmail.com>

import xml

# Базовый словарь, на случай, если нет файла
xml = '''<?xml version="1.0"?>

<data>

    <key>
        <ru>ключ</ru>
    </key>

    <space>
        <ru>пространство</ru>
    </space>

    <escape>
        <ru>побег</ru>
    </escape>

    <shift>
        <ru>сдвиг</ru>
    </shift>

</data>'''

import xml.etree.ElementTree as ET
root = ET.fromstring(xml)

#for child in root:
#    print(child.tag, ':', child.find('ru').text)
   
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
    for child in root:
        print(child.tag)
    print(u'введите любое из них:')
    eng_word = input()

    # Выдача перевода по ключу
    for child in root:
        if child.tag == eng_word:
            print(child.find('ru').text)

    print(u"Хотите узнать перевод другого слова?")
    if choice() == u"yes":
        interact()
    else:
        print(u"Bye")
        quit()

interact()
