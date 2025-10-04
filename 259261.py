def inverse_cade(n):
    grow(n)
    print(n)
    shrink(n)

grow = lambda x : f_then_g(grow,print,x//10)
shrink = lambda x :f_then_g(print,shrink,x//10)

def f_then_g(f,g,n):
    if n :
        f(n)
        g(n)


inverse_cade(123456)

    