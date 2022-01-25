from abc import ABC, abstractmethod


class AbstractClass(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def amount_material(self):
        pass


class Clothes(AbstractClass):

    def __init__(self, name):
        self.name = name


class Coat(Clothes):

    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    @property
    def amount_material(self):
        return self.size / 6.5 + 0.5


class Costume(Clothes):

    def __init__(self, name, height):
        super().__init__(name)
        self.height = height

    @property
    def amount_material(self):
        return self.height * 2 + 0.3


coat = Coat('asd', 175)
print(coat.name)
print(coat.amount_material)
cost = Costume('ad', 42)
print(cost.name)
print(cost.amount_material)
