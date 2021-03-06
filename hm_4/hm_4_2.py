"""
    1. Если в строке больше символов в нижнем регистре - вывести все в нижнем,
        если больше в верхнем - вывести все в верхнем,
        если поровну - вывести в противоположных регистрах.
    2. Если в строке каждое слово начинается с заглавной буквы, тогда
        добавить в начало строки 'done. '.
        Иначе заменить первые 5 элементов строки на 'draft: '.
    (можно использовать метод replace и/или конкатенацию строк + срезы)
    3. Если длина строки больше 20, то обрезать лишние символы до 20.
        Иначе дополнить строку символами '@' до длины 20.
    (можно использовать метод ljust либо конкатенацию и дублирование (+ и *))
    После выполнения кажого пункта выводить результат типа:
        1. Исходная строка: "some string".
        Результат: "some edited string".
    (Использовать форматирование строк f либо метод format)
"""

# можно заменить данную строку на input()
string = input('Введите текст: ')
a = 0
b = 0
for i in string:
    if i.isupper():
        a += 1
    else:
        b += 1
if a > b:
    result_1 = string.upper()
elif a < b:
    result_1 = string.lower()
else:
    result_1 = string.swapcase()
print('\n1) Исходная строка: ', string)
print('Результат: ', result_1)
if string.istitle():
    result_2 = 'done. ' + string
else:
    result_2 = string.replace(string[:5], 'draft: ')
print('\n2) Исходная строка: ', string)
print('Результат: ', result_2)
if len(string) >= 20:
    result_3 = string[:20]
else:
    result_3 = string.ljust(20, '@')
print('\n3) Исходная строка: ', string)
print('Результат: ', result_3)