class Car:
    def __init__(self, brand, model, year):
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__speed = 0

    # @property
    # def speed(self):
    #     return self.__speed

    # @speed.setter
    # def speed(self, speed):
    #     self.__speed = speed

    def speed_up(self):
        self.__speed += 5

    def speed_down(self):
        self.__speed -= 5

    def stop(self):
        self.__speed = 0

    def show_speed(self):
        print(self.__speed)

    def reverse(self):
        self.__speed = - self.__speed


my_car = Car('Acura', 'TSX', 2004)
my_car.show_speed()
my_car.speed_up()
my_car.show_speed()
my_car.speed_up()
my_car.show_speed()
my_car.speed_down()
my_car.show_speed()
my_car.stop()
my_car.show_speed()
my_car.speed_up()
my_car.show_speed()
my_car.reverse()
my_car.show_speed()
