from functools import lru_cache
@lru_cache(maxsize = 10240)
def fob(x):
    if x == 1:
        return 1
    elif x == 2:
        return 1
    else:
        return fob(x-1) + fob(x-2)
    
print(fob(1000))
print(fob.cache_info())
