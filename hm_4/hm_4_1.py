"""
    Вводится строка.
    1. Вывести количество слов в введенной строке.
    2. Вывести самое длинное слово и его длину.
"""
max_word = ''
string = input('Введите строку: ')
num = len(string.split())
print('Количество слов: ', num)
for i in string.split():
    if len(i) >= len(max_word):
        max_word = i
print('Самое длинное слово: ', '"', max_word, '"', 'его длина: ', len(max_word))
