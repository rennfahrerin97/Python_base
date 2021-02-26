"""
    Реализуйте игру Magic (hw3/magic.py) с некоторыми дополнениями.

    1. При запуске, программа спрашивает имя игрока.

    2. В словаре player_data хранить данные игрока и актуализировать их после
    каждой сыгранной игры. Оперировать такими данными:
        name - имя игрока
        games - общее количество сыграных игр
        record - рекордное количество попыток (минимальное)
        avg_attempts - среднее количество попыток за игру

    3. При выходе из программы данные игрока записывать в файл (txt либо json).

    **4. При запуске программы, после ввода имени пользователем, читать файл,
    если данные об игроке есть в файле то загружать их в player_data.

"""
def game_magic(name, games, record, avg_attempts):

    import random
    random_number = random.randint(1, 100)  # случайное число от 1 до 100
    counter = 0  # счетчик попыток
    games += 1
    while True:
        try:
            number = int(input("The Magic number is: "))
            counter += 1
            print(random_number)
        except ValueError:
            print("\nYou must enter a number.")
            game_magic(input("The Magic number is: "), player_data)
        if number > random_number:
            print("\nNo, the Magic number less than:", number)
            continue
        elif number < random_number:
            print("\nNo, the Magic number greater than:", number)
            continue
        else:
            print("\nCongratulations! The Magic number is -", number)
            print("Attempts:", counter)
            if counter <= record:
                record = counter
            avg_attempts += counter
            print("Record:", record)
            print("Avg_attempts:", round(avg_attempts / games))
            print("Played games:", games)
            player_data = {"name": name, "games": games, "record": record, "avg_attempts": avg_attempts}
            if input("\nContinue? (y/n) ") != "y":
                return player_data
        break
    return game_magic(name, games, record, avg_attempts)

def main():
    print("Guess the Magic number!\n")
    name = input("Please, enter your name: ")
    games = 0
    record = 100
    avg_attempts = 0
    user = game_magic(name, games, record, avg_attempts)
    with open("questionnaire.txt", "a+") as f:
        print(str(user), file=f)
    print('Bye, ', name, '!')

if __name__ == '__main__':
    main


