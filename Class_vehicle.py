class Vehicle:

    def __init__(self, name, mileage):
        self.name = name
        self.mileage = mileage


    def get_vehicle_type(self, wheels):
        if wheels == 2:
            return f"Это мотоцикл марки {self.name}"
        elif wheels == 3:
            return f"Это трицикл марки {self.name}"
        elif wheels == 4:
            return f"Это автомобиль марки {self.name}"
        elif wheels > 4:
            return f"Я не знаю такого транспортного средства"
        else:
            return f"Некорректные данные"

    def get_vehicle_advice(self, mileage):
        if mileage <= 50000:
            return f"Неплохо {self.name}, можно брать"
        elif  50001 <= mileage <= 100000:
            return f"{self.name}, надо внимательно проверить"
        elif 100001 <= mileage <= 150000:
            return f"{self.name}, надо провести полную диагностику"
        elif 150000 < mileage:
            return f"{self.name} лучше не покупать"
        else:
            return "Некорректные данные"


vehicle_1 = Vehicle("Toyota", 49000)
print(vehicle_1.get_vehicle_type(2))
print(vehicle_1.get_vehicle_advice(49000))
print()

vehicle_2 = Vehicle("Lada", 85000)
print(vehicle_2.get_vehicle_type(4))
print(vehicle_2.get_vehicle_advice(85000))
print()

vehicle_3 = Vehicle("BMW", 101000)
print(vehicle_3.get_vehicle_type(3))
print(vehicle_3.get_vehicle_advice(101000))
print()

vehicle_4 = Vehicle("Opel", 200000)
print(vehicle_4.get_vehicle_type(7))
print(vehicle_4.get_vehicle_advice(200000))
print()














