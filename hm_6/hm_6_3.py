"""
    Текстовый файл (phone_book.txt) содержит список из имен и номеров телефона.
    Переписать в файл (edited_phone_book.txt) данные владельцев,
    чьи имена начинаются на букву "m" либо заканчиваются на "а"
    (регистр не имеет значения).
    В файл записывать данные в таком формате:
    1. +380501234561 - Имя
    2. +380501234562 - Имя
    3. +380501234563 - Имя
    4. +380501234564 - Имя
"""


def main():
    phone = ""
    name = ""
    with open("phone_book.txt", "r+") as f_1:
        s = list(f_1.readlines())
        with open("edited_phone_book.txt", "w+") as f_2:
            for i in s:
                j = list(i)
                for j in i:
                    if j.isdigit(): phone += j
                    if j.isalpha(): name += j
                name = name.title()
                if name[0] == "M" or name[-1] == "a":
                    phone = "+380" + phone[-9:]
                    f_2.write(f"{phone} - {name}\n")
                phone = ""
                name = ""


if __name__ == "__main__":
    main()
