def main():

    import random
    import string

    from pathlib import Path
    path = Path(__file__).resolve()
    path = path.parent
    file_path = path / "memory.txt"
    with open(file_path, "w+") as f:
        f.write("Здесь хранятся все сгенерированые пароли\n")

    def gen_password(chars, length=8):
        password = ""
        for i in range(length):
            password += random.choice(chars)
        return password

    def gen_strong_pw():
        length = random.randint(8, 16)
        password = gen_password(string.digits + string.ascii_letters + string.punctuation, length)

        counter_d = counter_u = counter_l = counter_s = 0
        for char in password:
            if char.isdigit():
                counter_d += 1
            elif char.isupper():
                counter_u += 1
            elif char.islower():
                counter_l += 1
            elif not char.isspace():
                counter_s += 1

        if counter_d and counter_u and counter_l and counter_s:
            return password
        return gen_strong_pw()

    def base():
        choice = input(
            "1. Сгенерировать простой пароль\n"
            "2. Сгенерировать средний пароль\n"
            "3. Сгенерировать сложный пароль\n"
        )
        if choice == "1":
            password = gen_password(string.ascii_lowercase)
        elif choice == "2":
            password = gen_password(string.ascii_letters + string.digits)
        elif choice == "3":
            password = gen_strong_pw()

        with open(file_path, "r+") as f:
            last_password = f.read()
            last_password = list(last_password)
            for i in last_password:
                if i == password:
                    print("Ненадёжный пароль!")
                else:
                    f.write(f"{password}\n")
        print(password)
        if input("Завершить генерацию?") != "y":
            base()
    return

    base()

if __name__ == "__main__":
    main()
