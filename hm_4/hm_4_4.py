string = 'Lorem, Ipsum, is, simply, dummy, text, of, the, printing, industry.'
# 1. Изменить строку таким образом, чтоб вместо ', ' был пробел ' '
#    Результат: 'Lorem Ipsum is simply dummy text of the printing industry.'
string = string.replace(',', '')
print(string)

# 2. Найти индекс самой последней буквы 's' в строке.
#    Результат: 53
print(string.rfind('s'))

# 3. Найти количество букв 'i' в строке (регистр не имеет значения).
#    Результат: 6
result_3 = string.count('i') + string.count('I')
print(result_3)

# 4. Найти и вывести срез строки.
#    Результат: 'simply dummy text'
#    (используйте методы find или index для получения индексов)
a = string.find('sim')
b = string.index(' of')
print(string[a:b])
# 5. Продублируйте первую половину строки 3 раза и склейте с второй половиной
#    и выведите на экран.
#    Результат: 'Lorem Ipsum is simply dummy tLorem
#    Ipsum is simply dummy tLorem Ipsum is simply dummy text of the printing industry.'
c = int(len(string) / 2)
result_5 = string[:c] * 3 + string[c:]
print(result_5)
