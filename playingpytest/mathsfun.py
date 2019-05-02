class BasicMaths:
    '''
    Some basic maths functions to use with pytest
    '''

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(x, y):
        a = x + y
        print(a)
        return a

    def subtract(x, y):
        a = x - y
        print(a)
        return a

    def divide(x, y):
        a = x / y
        print(a)
        return a

    def floordiv(x, y):
        a = x // y
        print(a)
        return a

    def exponent(x, y):
        a = x ** y
        print(a)
        return a
