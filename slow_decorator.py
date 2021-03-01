"""
    Реализовать декораторы:
    1. @time_decorator - считает и выводит время работы функции,
        если функция выполняется дольше 5 секунд, тогда дополнительно
        выводить сообщение print(f'{func.__name__} - very slow function')

    * в func.__name__ лежит название функции

    2. @slow_decorator - замедляет выполнение функции на 5 секунд

    Используйте библиотеку time, а именно функции time и sleep

"""
import time

def time_decorator(func):

    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)  # вызывается задекорированная функция
        end = time.time() - start
        if end >= 5:
            print(f'{func.__name__} - very slow function')
        return result

    return wrapper

def slow_decorator(func):

    def wrapper(*args, **kwargs):

        time.sleep(5)
        result = func(*args, **kwargs)
        return result

    return wrapper

# Як тест, застосовано до задачі grade_journal
def main():

    @time_decorator
    def input_students(students):
        list_students = {}
        for i in range(students):
            s = input().split(" ")
            list_students[int(s[1])] = s[0]
        return list_students

    @slow_decorator
    def sort_mark(list_students):
        list_st = list(list_students.keys())
        list_st.sort(reverse=True)
        tmp_data = {}
        for i in list_st:
            tmp_data[i] = list_students[i]
        return tmp_data

    students = int(input("Введите количество студентов: "))
    print("\nВведите фамилии и оценки через пробел:")
    grade = sort_mark(input_students(students))
    i = 0
    for item in grade.values():
        if i != students:
            i += 1
            print(f"{i}. {item}")

if __name__ == "__main__":
    main()