from math import sqrt

def has_big_sqrt(x):
    return x > 0 and sqrt(x) >= 10

x = -1000

print(has_big_sqrt(x))

def reasonable(n):
    return n != 0 and  1/n != 0 

n = 0

def makeadder(a):
    def adder(x):
        return x + a
        
    return adder

print(makeadder(3)(12))

