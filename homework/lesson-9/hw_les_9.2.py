class Road():
    def __init__(self, x, y, weight, z):
        self._x = x
        self._y = y
        self._weight = weight
        self._z = z

    def mass(self):
        print(f'{(self._x * self._y * self._weight * self._z) / 1000}т.')


first_road = Road(1000, 50, 20, 5)
first_road.mass()
