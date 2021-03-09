"""
    1. Реализуйте класс Car с атрибутами:
    - brand (марка)
    - model (модель)
    - engine (объем двигателя)
    - year (год выпуска)
    2. Создайте метод get_info,
        "Ford Focus v2.3", где 2.3 - объем двигателя (engine)
    3. Создайте список из 5 объектов класса Car.
    4. Отсортируйте список объектов по year
    5. Выведите на экран результат метода get_info для каждого объекта списка
"""
class Car:

    def __init__(self, brand, model, engine, year=2021):
        self.brand = brand
        self.model = model
        self.engine = engine
        self.year = year

    def __str__(self):
        return self.get_info()

    def get_info(self):
        print(f"{self.brand} {self.model} {self.engine}")

car = Car("Ford", "Focus", "v2.3").get_info()

list_car = [
Car("MITSUBISHI", "Lancer", "v2.0", 2008),
Car("Chevrolet", "Impala", "v6.7", 1969),
Car("Audi", "TT", "v2.0", 2021),
Car("Tesla", "X P90D", "0", 2016),
Car("БОГДАН", "А091", "v4.0", 2006)
    ]

list_car = sorted(list_car, key=lambda car: car.year)

for car in list_car:
    car.get_info()
