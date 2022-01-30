class ComplexNum:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f'{self.a + other.a}+{self.b + other.b}i'

    def __mul__(self, other):
        if (self.a * other.a - self.b * other.b) < 0:
            return f'{self.a * other.b + self.b * other.a}i' \
                   f'{self.a * other.a - self.b * other.b}'
        elif (self.a * other.a - self.b * other.b) == 0:
            return f'{self.a * other.b + self.b * other.a}i'
        else:
            return f'{self.a * other.a - self.b * other.b}+' \
                   f'{self.a * other.b + self.b * other.a}i'


a = ComplexNum(1, 2)
b = ComplexNum(1, 2)
print(a + b)
print(a * b)
