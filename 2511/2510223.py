def fib(n):
    if n==0 or n==1:
        return n
    else:
        return fib(n-1)+fib(n-2)
    
def memo(f):
    cache = {}
    def memoryf(x):
        if not x in cache:
            cache[x] = f(x)
            return f(x)
        else:
            return cache[x]
    return memoryf

print(memo(fib)(10))

        
