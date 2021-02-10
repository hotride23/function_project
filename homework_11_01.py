class TV:
    def __init__(self, brand, size, cost):
        self.__cost = cost
        self.__brand = brand
        self.__size = size
        self.status = 'off'

    @property
    def cost(self):
        return self.__cost

    @cost.setter
    def cost(self, cost):
        self.__cost = cost

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, brand):
        self.__brand = brand

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        self.__size = size

    def turn_on(self):
        self.status = 'on'

    def turn_off(self):
        self.status = 'off'


mitv55 = TV('xiaomi', 55, '500$')
print(mitv55.size)
mitv55.size = 60
print(mitv55.size)
mitv55.turn_on()
print(mitv55.status)
mitv55.turn_off()
print(mitv55.status)
