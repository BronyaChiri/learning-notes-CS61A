def cycle(f1,f2,f3):
    def g(n):
        def h(x):
            if n == 0 :
                return x
            elif n == 1 :
                return f1(x)
            elif n == 2 :
                return f2(f1(x))
            elif n == 3 :
                return f3(f2(f1(x)))
            elif n == 4 :
                return f1(f3(f2(f1(x))))
            
        return h
        
    return g
