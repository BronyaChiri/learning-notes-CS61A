def square(x):
    return x**2

def search(f):
    x = 0 
    while  not f(x):
        x += 1

    return x
    

def inverse(f):
    return lambda y : search( lambda x : f(x) == y )



sqrt = inverse(square)
print(sqrt(25**2))