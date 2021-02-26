"""
    1. Реализовать функцию get_country(city), которая принимает название города
    и возвращает страну, которой он принадлежит исходя из словаря data.

    2. Релизовать функцию groupping_data(data), которая принимает словарь data
    и возвращает отформатированные данные в виде списка словарей с ключами
    'country', 'capital' и 'cities'.
    Учитывать, что во входящем словаре data
    ключ - country, первый элемент значения - capital, остальные - cities.
"""

data = {
    "Ukraine": ["Kiev", "Kharkiv", "Odesa", "Dnipro"],
    "France": ["Paris", "Marseille", "Lyon", "Toulouse"],
    "Austria": ["Vienna", "Graz", "Linz", "Salzburg"],
    "Germany": ["Berlin", "Hamburg", "Munich", "Frankfurt"],
}


def get_country(city):
    country = ''
    for key, value in data.items():
        for i in value:
            if i == city:
                country = key
    return country

def groupping_data(data_1):
    country = ""
    capital = ""
    data_corect = []
    for key, value in data.items():
        cities = []
        country = key
        for i in value:
            if value.index(i) == 0:
                capital = i
            else:
                cities.append(i)
        data_2 = {"country": country, "capital": capital, "cities": cities}
        data_corect.append(data_2)
    return data_corect




