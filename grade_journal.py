"""
    Пользователь вводит количество студентов N.
    После чего вводит N строк, в которых записана фамилия и балл через пробел.

    Программа выводит список фамилий, отсортированный по их баллам по убыванию.

    Пример:

    [out] Введите количество студентов:
    [in]  3

    [out] Введите фамилию и балл:
    [in]  Иванов 87

    [out] Введите фамилию и балл:
    [in]  Смирнов 90

    [out] Введите фамилию и балл:
    [in]  Фролов 89

    [out]
        1. Смирнов
        2. Фролов
        3. Иванов
"""
def main():

    # функція приймає кількість студентів і словник з їхніми даними
    def input_students(students):
        list_students = {}
        for i in range(students):
            s = input().split(" ")
            list_students[int(s[1])] = s[0]
        return list_students

    # функція приймає словник з даними студентів та сортує їх в порядку спадання. повертає відсортований словник
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
