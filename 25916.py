def square(x):
    return x**2

def increment(x):
    return x+1

def triple(x):
    return 3*x

def product(i , term):
    a , total = 1 , 1
    while a <= i :
        total = total*term(a)
        a += 1

    return total 

print(product(5,increment))
