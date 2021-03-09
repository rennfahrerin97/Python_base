"""
    Для того, чтобы больше попрактиковаться с классами
    воспользуйтесь задачником http://www.itmathrepetitor.ru/zadachi-na-klassy/
    Реализуйте класс Alphabet.
    Алфавит имеет такие атрибуты (создаются в конструкторе __init__):
    - language (язык)
    - letters (список букв алфавита)
    Объект алфавита может (методы):
    - вывести все буквы алфавита
    - посчитать количество букв алфавита
    - определять, относится ли буква к этому алфавиту
"""
class Alphabet:

    def __init__(self, language, letters):
        self.language = language
        self.letters = letters
        self.abc_EN = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.abc_UA = "АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ"
        self.abc_RU = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

    def print_ABC(self):
        alphabet = ""
        if self.language == "EN":
            alphabet = self.abc_EN
        elif self.language == "UA":
            alphabet = self.abc_UA
        elif self.language == "RU":
            alphabet = self.abc_RU
        else:
            print("Fail entering!")
        abc = ""
        for i in alphabet:
            abc += i + ", "
        print(abc)

    def count_ABC(self):
        if self.language == "EN":
            print("26")
        elif self.language == "UA":
            print("33")
        elif self.language == "RU":
            print("33")
        else:
            print("Fail entering!")


    def find_letter(self):
        if self.abc_EN.find(self.letters):
            self.language = "EN"
        elif self.abc_UA.find(self.letters):
            self.language = "UA"
        elif self.abc_RU.find(self.letters):
            self.language = "RU"
        else:
            print("Fail entering!")
        print(self.language)

c = Alphabet("EN", "t")

c.print_ABC()

c.count_ABC()

c.find_letter()