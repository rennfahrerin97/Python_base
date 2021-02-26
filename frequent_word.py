"""
    Реализуйте функцию, которая принимает текст и возвращает слово, которое
    в этом тексте встречается чаще всего.

    Напишите несколько тестов для функции.

    # Если таких слов несколько - приоритет у первого, если расположить список
    # в алфавитном порядке.
    # Например:
    text = "hi world, hi python. i am very cool but i am still learning."
    # чаще всего встречаются "hi", "i" и "am", но по алфавиту "am" - раньше
    assert frequent_word(text) == "am"

"""
# ф-ція, що визначає яка за алфавітним порядком перша буква слова - алфавіт англійський.
# Приймає слово, повертає цифру.
def ABC(char):
    char = list(char)
    import string
    abc = {}
    letter = 1
    for i in string.ascii_lowercase:
        abc[i] = letter
        letter += 1
    for key, value in abc.items():
        if key == char[0]:
            letter = value
    return letter

# ф-ція, що відділяє слова від знаків пунктуації. Приймає стрічку, повертає список
def list_text(string):
    text_correct = []
    word = ""
    for i in string + " ":
        if i.isalnum() or i == "'":
            word += i.lower()
            continue
        else:
            if word != "":
                text_correct.append(word)
        word = ""
    return text_correct

# ф-ція, що рахує скільки раз слово повторюється в реченні. Приймає список, повертає словник.
def count_words(list_words):
    data = {}
    for words in list_words:
        if words in data.keys():
            count = data[words]
            count += 1
        else:
            count = 1
        data[words] = count
    return data

# ф-ція, що приймає словник слово: к-сть раз його повторень та повертає слово, що має найбільше раз повторень.
# Якщо таких слів кілька - повертає те, що стоїть перше по алфавіту.
def count_ABC(data):
    popular_word = 0
    data_final = {}
    for key, value in data.items():
        if value >= popular_word:
            popular_word = value
            data_final[key] = ABC(key)
    popular_word = 26
    word = ""
    for key, value in data_final.items():
        if value <= popular_word:
            popular_word = value
            word = key
    return word

"""
    Реализуйте функцию, которая принимает текст и возвращает слово, которое
    в этом тексте встречается чаще всего.
"""
def frequent_word(text):
    text_in_list = list_text(text)
    data = count_words(text_in_list)
    word = count_ABC(data)
    return word

t_1 = "He had beautiful black hair. He liked motorbikes. He was kind to apples, oranges and little girls."
assert frequent_word(t_1) == "he"

t_2 = "hi world, hi python. i am very cool but i am still learning."
assert frequent_word(t_2) == "am"

t_3 = "Process finished with exit code."
assert frequent_word(t_3) == "code"

print("All tests passed successfully!")