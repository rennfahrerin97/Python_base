"""
    Генератор паролей.
    Пользователь выбирает 1 из 3 вариантов:
    1. Сгенерировать простой пароль (только буквы в нижнем регистре, 8 символов)
    2. Сгенерировать средний пароль (любые буквы и цифры, 8 символов)
    3. Сгенерировать сложный пароль (минимум 1 большая буква, 1 маленькая, 1 цифра и 1 спец-символ, длина от 8 до 16 символов)
        (для 3 пункта можно генерировать пароли до тех пор, пока не выполнится условие)
    Для решения использовать:
    - константы строк из модуля string (ascii_letters, digits и т.д.)
    - функцию choice из модуля random (для выборки случайного элемента из последовательности)
    - функцию randint из модуля random (для генерации случайной длины сложного пароля от 8 до 16 символов)
    Дополнительно:
    1. Позволить пользователю выбирать длину пароля, но предупреждать, что
        пароль ненадежный, если длина меньше 8 символов
    2. Добавить еще вариант генерации пароля - 4. Пользовательский пароль:
        - пользователь вводил пул символов, из которых будет генерироваться пароль
        - вводит длину желаемого пароля
        - программа генерирует пароль из нужной длины из введенных символов
        - * игнорируются пробелы
"""  # noqa: E501
# def main():
#     pass
# if __name__ == '__main__':
#     main

import string
vocabulary = string.ascii_letters
digit = string.digits
char = string.punctuation
password = ''
i = 0
a = 0
b = 0
c = 0
d = 0
import random
while True:
    choice = input("1. Сгенерировать простой пароль.\n"
                   "2. Сгенерировать средний пароль.\n"
                   "3. Сгенерировать сложный пароль.\n")
    if choice == '1':
        while i < 8:
            password += random.choice(vocabulary)
            i += 1
        print(password.lower())
        exit(print('\nПароль сгенерирован.'))
    elif choice == '2':
        while i < 8:
            password += random.choice(vocabulary + digit)
            i += 1
        print(password)
        exit(print('\nПароль сгенерирован.'))
    elif choice == '3':
        while True:
            while i < random.randint(8, 16):
                password += random.choice(vocabulary + digit + char)
                i += 1
            for j in password:
                if j.isupper():
                    a += 1
                if j.islower():
                    b += 1
                if j.isdigit():
                    c += 1
                if char.find(j):
                    d += 1
            if a >= 1 and b >= 1 and c >= 1 and d >= 1:
                print(password)
                exit(print('\nПароль сгенерирован.'))
            else:
                continue
            break
    else:
        if input('\nОшибка ввода! Повторить? (y/N) \n') != 'y':
            break
