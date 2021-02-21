"""
    Обновите форму регистрации из hw5/reg_form.py таким образом, чтобы:
    1. Все данные пользователей сохранялись в файл users.txt в любом формате.
    2. В файл errors.txt записывать все ошибочные либо не валидные вводы.
        (не валидный номер телефона, email и т.д.)
"""
import re

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


def main():
    user_list = []

    while True:
        phone = get_phone()
        email = get_email()
        password = get_password()

        user_list.append([phone, email, password])
        save_data(phone, email, password)

        print(
            f"\nПоздравляем с успешной регистрацией!"
            f"\nВаш номер телефона: +{phone}"
            f"\nВаш email: {email}"
            f'\nВаш пароль: {"*"*len(password)}'
        )

        if input("Продолжить? (Y/n)") == "n":
            break

def save_data(phone, email, password):
    with open(BASE_DIR / "users.txt", "a") as f:
        print(f"{phone} {email} {password}", file=f)

def error_enter(error, name_error):
    with open(BASE_DIR / "errors.txt", "a") as f:
        print(f"{name_error}:{error}", file=f)

def get_phone():
    phone = input("Введите номер телефона:")
    a = "".join(s for s in phone if s.isdigit())
    phone = "38" + a[-10:]

    if len(phone) != 12:
        print("Неверный формат. Повторите ввод.")
        error_enter(phone, "Телефон")
        return get_phone()
    return phone


def get_email():
    email = input("Введите email: ")
    if len(email) < 6 or email.count("@") != 1 or email.startswith("@"):
        print("Неверный формат. Повторите ввод.")
        error_enter(email, "Email")
        return get_email()
    return email

def get_password():
    password = input("Введите пароль: ")
    if len(password) < 8 or re.findall(r"\s", password):
        print("Пароль слишком простой. Придумайте более надежный пароль.")
        error_enter(password, "Пароль")
        return get_password()

    u_counter = l_counter = d_counter = s_counter = 0
    for i in password:
        if i.isupper():
            u_counter += 1
        elif i.islower():
            l_counter += 1
        elif i.isdigit():
            d_counter += 1
        else:
            s_counter += 1

    if min(u_counter, l_counter, d_counter, s_counter) == 0:
        print("Пароль слишком простой. Придумайте более надежный пароль.")
        return get_password()

    if input("Повторите пароль: ") != password:
        print("Пароли не совпадают.")
        return get_password()
    return password


if __name__ == "__main__":
    main()
