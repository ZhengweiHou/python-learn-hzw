class Money:
    def __init__(self, number=0):
        self.number = number

    def __add__(self, other):
        print('加法')
        if isinstance(other, Money):
            self.number += other.number
        elif isinstance(other, (int, float)):
            self.number += other

    def __sub__(self, other):
        print('减法')
        if isinstance(other, Money):
            self.number -= other.number
        elif isinstance(other, (int, float)):
            self.number -= other

    def __mul__(self, other):
        print('乘法')
        self.number *= other


m = Money(1)

m + Money(10)
print(m.number)

m + 12
print(m.number)

m - 5
print(m.number)

m * 2
print(m.number)
