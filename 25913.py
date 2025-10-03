def apply_twice(f,x):
    return f(f(x))

def square(x):
    return x**2

print(apply_twice(square,4))