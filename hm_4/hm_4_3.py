
"""
    Написать программу, которая принимает номер телефона в любом формате:
    +38 (050) 12-34-567 или 099 123 -45 67 или 80501234567 или 888 050 123 4567
    а выводит в форма  4567.
    Если цифр в номере недоте: 38050123статочно, чтобы описать номер в нужном формате -
        попросить пользователя повторить ввод.
"""
while True:
    phone_1 = ''
    phone = input('Enter phone number: ')
    for i in phone:
        if i.isdigit():
            phone_1 += i
    if phone_1[0] == '3' and len(phone_1) == 12:
        pass
    elif phone_1[0] == '8' and len(phone_1) == 11:
        phone_1 = '3' + phone_1
    elif phone_1[0] == '0' and len(phone_1) == 10:
        phone_1 = '38' + phone_1
    else:
        print('Incorrect entering!\n')
        continue
    print(phone_1)
    break
