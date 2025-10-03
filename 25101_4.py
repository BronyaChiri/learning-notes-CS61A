from math import *

'''
def count(x):
    if x <= 1:
        return 0 
    else:

        if x % 10 == 8:
            return 1 + count(x // 10)
        else:
            return count(x//10)
        
print(count(8812378947938))
'''
'''
def distance(x):
    if x <= 9:
        return 0
    else:
        last , second_last = x % 10 , (x // 10) % 10
        return abs(last - second_last) + distance(x//10)
    
print(distance(31415))
'''
'''
def summ(x,f,g,i=1):
    if x >= i:
        if i % 2 == 1:
            return f(i) + summ(x,f,g,i+1)
        else:
            return g(i) + summ(x,f,g,i+1)
    else:
        return 0


square = lambda x: x*x
triple = lambda x: x*3

print(summ(4, square,triple)) 
'''







