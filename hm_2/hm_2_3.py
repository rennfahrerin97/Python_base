"""
    Вводится число от 1 до 999
    (если введено не число либо число вне диапазона - вывести сообщение)
    1. Найти сумму цифр числа.
    2. Вывести на экран, порядок, в котором расположены цифры числа
        (возростание/убывание/в разброс(равны))
"""
i = None
a = input('Введіть число від 1 до 999: ')
while i is None:
    try:
        a = int(a)
        while (a < 1) or (a > 999):
            print('Введено некоректне значення!!! Будь ласка, повторіть введення.')
            a = int(input('Введіть число від 1 до 999: '))
    except ValueError:
        print('Введено некоректне значення!!! Будь ласка, повторіть введення.')
        a = input('Введіть число від 1 до 999: ')
    else:
        i = 1
        print()
        b = a // 100
        c = (a % 100) // 10
        d = (a % 100) % 10
        print('Сума цифер числа', a, ':', b + c + d)
        if b == c == d or (b == 0 and c == d):
            print('Всі цифри числа', a, 'рівні')
        elif (b > c) and (c > d) or (b == 0) and (c > d):
            print('Всі цифри числа', a, 'розміщені в порядку спадання.')
        elif (b < c) and (c < d) or (b == 0) and (c < d) and (c != 0):
            print('Всі цифри числа', a, 'розміщені в порядку зростання.')
        elif b == c == 0:
            print('Число', a, '- натуральне число.')
        else:
            print('Всі цифри числа', a, 'розміщенні стахостично.')