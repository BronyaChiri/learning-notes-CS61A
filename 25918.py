"""from ucb import trace
@trace
"""


def remove(n,digit):
    kept , digits = 0 , 0
    while n >= 1 :
        last , n= n%10 , n//10 
        if last != digit :
            kept += 1
            digits += 10 ** (kept-1)*last

    return digits

print(remove(234593209,9))