data = [
    (2, "green"),
    (1, "blue"),
    (2, "yellow"),
    (1, "aquamarine"),
    (4, "red"),
    (3, "gold"),
    (5, "black"),
    (2, "brown"),
    (5, "pink"),
    (1, "purple"),
    (4, "white"),
    (1, "gray"),
]


# 1. Вывести список data, отсортированный по цвету (2 элемент кортежа).
print(sorted(data, key=lambda data: data[1]))
# 2. Отсортировать список по 1 элементу кортежа, а если значения одинаковые,
#    то их отсортировать по 2 элементу. Результат вывести на экран.
print(sorted(data, key=lambda data: (data[0], data[1])))
# 3. С помощью filter() и lambda вывести только те кортежи из списка,
#    цвет которых состоит из 4 букв.
print(list(filter(lambda data: len(data[1]) == 4, data)))
# 4. Вывести цвет, которой состоит из найбольшего количества букв.
color = []
for i in data:
    color.append(i[1])
print(max(color, key=len))
