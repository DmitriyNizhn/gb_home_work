class Car():
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} поехала')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn(self, direction):
        print(f'{self.name} повернула на {direction}')

    def show_speed(self):
        print(f'скорость авто {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed >= 60:
            print(f'скорость автомобиля {self.speed} превышение на {self.speed - 60}')
        else:
            print(f'скорость авто {self.speed}')


class WorkCar(Car):
    def show_speed(self):
        if self.speed >= 40:
            print(f'скорость автомобиля {self.speed} превышение на {self.speed - 40}')
        else:
            print(f'скорость авто {self.speed}')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police


class SportCar(Car):
    None


# car_1 = Car(100, 'red', 'mazda')
# car_1.turn('лево')
# car_1.go()
# car_1.stop()
# print(car_1.name)
# car_1.show_speed()
car_2 = TownCar(100, 'red', 'BMW')
car_2.turn('лево')
car_2.go()
car_2.stop()
print(car_2.name)
car_2.show_speed()
car_3 = WorkCar(150, 'red', 'Fiat')
car_3.turn('право')
car_3.go()
car_3.stop()
print(car_3.name)
car_3.show_speed()
car_4 = SportCar(150, 'red', 'Porsche')
car_4.turn('право')
car_4.go()
car_4.stop()
print(car_4.name)
car_4.show_speed()

car_5 = PoliceCar(100, 'white', 'chevrolet')
car_5.turn('право')
car_5.go()
car_5.stop()
print(car_5.name)
car_5.show_speed()
print(car_5.is_police)
