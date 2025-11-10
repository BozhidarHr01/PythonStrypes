from math import exp
class InvalidRangeException(Exception):
    def __init__(self, msg):
        self.message = msg
        super().__init__(self.message)

def func(x):
    return x*x*x + 3*x - 5
    return exp(x) - 2*x - 2

def bisection(a, b, eps):
    if (func(a) * func(b) >= 0):
        raise InvalidRangeException("Invalid range [a, b]")

    c = a
    while((b - a) >= eps):
        c = (a + b) / 2

        if (func(c) == 0.0):
            break
        
        if(func(c) * func(a) < 0):
            b = c
        else:
            a = c
    return c

try:
    a = input("insert a: ")
    b = input("insert b: ")
    eps = 0.001
    print(bisection(int(a), int(b), eps))
except ZeroDivisionError as e:
    print("Cannot divide by zero!")
except ValueError as e:
    print("Invalid a and b")