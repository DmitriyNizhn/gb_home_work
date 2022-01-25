class Cell:
    def __init__(self, count):
        self.count = count

    def make_order(self, q_array):
        return ('*' * q_array + '\\n') * (self.count // q_array) \
               + ('*' * (self.count % q_array))

    def __add__(self, other):
        return self.count + other.count

    def __sub__(self, other):
        return self.count - other.count if \
            (self.count - other.count) > 0 else \
            'Разность не больше нуля'

    def __mul__(self, other):
        return self.count * other.count

    def __floordiv__(self, other):
        return self.count // other.count


a = Cell(10)
b = Cell(15)

print(b // a)
