"""
    1.
    Создать файл file_practice.txt
    Записать в него строку 'Starting practice with files'
    Файл должен заканчиваться пустой строкой
"""
from pathlib import Path
path = Path(__file__).resolve()
path = path.parent
file_path = path / "file_practice.txt"
with open(file_path, "w") as f:
    f.write("Starting practice with files\n")
"""
    2.
    Прочесть первые 5 символов файла и вывести содержимое в верхнем регистре
    Затем прочесть весь файл от начала до конца, вывести содержимое на экран 
"""
with open("file_practice.txt", "r+") as f:
    print(f.read(5).upper())
    f.seek(0)
    print(f.read())
"""
    3.
    Прочесть файл files/text.txt
    В тексте заменить все буквы 'i' на 'e', если 'i' большее кол-во,
    иначе - заменить все буквы 'e' на 'i'
    Полученный текст дописать в файл file_practice.txt
"""
i = 0
e = 0
with open("text.txt", "r") as f:
    data = f.read()
for k in data:
    if k == "i":
        i += 1
    if k == "e":
        e += 1
if i > e:
    with open("file_practice.txt", "a+") as f:
        f.write(data.replace('i', 'e'))
if i < e:
    with open("file_practice.txt", "a+") as f:
        f.write(data.replace('e', 'i'))
"""
    4.
    Если в файле file_practice.txt четное количество элементов
    - файл должен заканчиваться строкой 'the end', иначе - строкой 'bye'
    Прочесть весь файл и вывести содержимое
"""
with open("file_practice.txt", "r+") as f:
    data = f.read()
    elements = f.tell()
    if elements % 2 == 0:
        f.seek(elements)
        f.write("the end\n")
    else:
        f.seek(elements)
        f.write("bye\n")
    f.seek(0)
    print(f.read())
"""
    5.
    В средину файла file_practice.txt вставить строку " *some inserted text* "
    (средина - имеется в виду средина текста)
"""
with open("file_practice.txt", "r+") as f:
    data_1 = (f.read(round(elements/2)))
    data_2 = f.read()
    data = data_1 + '\n*some inserted text*\n' + data_2
    print(data)
