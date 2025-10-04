from operator import add , mul
from math import pi , sin


def sum_square(x,y):
    return square(x) + square(y)

def square(x):
    return mul(x,x)

def area(radius):
    return pi*(radius**2)

value = square(13)
print(value)
print(sum_square(3,19))
print(sin(area(3)))
print(print(1),print(2))