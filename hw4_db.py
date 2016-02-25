#4.2. задание по БД - через def
import pickle

# Базовый словарь, на случай, если нет файла
en_ru_dump = {
        'key': {'ключ','клавиша','код',},
        'space': {'пространство','космос','пробел',},
        'escape': {'побег','выход','спасение'},
        'shift': {'сдвиг','изменение','переключение'},
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
    choice = input('Да: Enter, 1, Y, y / Нет - любая другая клавиша\n')
    choice = choice.lower()
    yes = ['', 'да', '', '1', 'y', 'yes']

    if choice in yes:
        choice = 'yes'
    else:
        choice = 'no'
    return choice

# Функция интерактивного общения со словарем
def interact():
    # Поиск по ключу
    print('Чтобы узнать перевод слов:')
    for k in en_ru_new.keys():
        print('\t',k)
    print('введите любое из них:')
    eng_word = input()

    # Выдача перевода по ключу
    if eng_word in en_ru_new.keys():
        print(eng_word, ':',en_ru_new.get(eng_word))
    else:
        print('Слова', eng_word, 'нет в словаре')

    print("Хотите узнать перевод другого слова?")
    if choice() == "yes":
        interact()
    else:
        print("Bye")
        quit()

interact()
