"""
    Написать функцию, которая будет проверять счастливый билетик или нет.
    Билет счастливый, если сумма одной половины цифр равняется сумме второй.
"""


def is_lucky(ticket_num):
    ticket_num = list(str(ticket_num))
    center = len(ticket_num) // 2
    ticket_num_1 = ticket_num[:center]
    ticket_num_2 = ticket_num[center:]
    sum_1 = 0
    sum_2 = 0
    for i in ticket_num_1:
        i = int(i)
        sum_1 += i
    for i in ticket_num_2:
        i = int(i)
        sum_2 += i
    return sum_1 == sum_2

assert is_lucky(1230) is True
assert is_lucky(239017) is False
assert is_lucky(134008) is True
assert is_lucky(15) is False
assert is_lucky(2020) is True
assert is_lucky(199999) is False
assert is_lucky(77) is True
assert is_lucky(479974) is True

print("All tests passed successfully!")
