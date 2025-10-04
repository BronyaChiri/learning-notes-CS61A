from operator import floordiv , mod
x,y,z = 8 , 0 , -11
def absolute_value(x):
    if x < 0 :
        return -x
    elif x == 0 :
        return 0
    else :
        return x
    
x=absolute_value(x)
y=absolute_value(y)
z=absolute_value(z)

print(x,y,z)
i , total = 0 , 0
while i <= 99:
    i += 1
    total += i

print(total)

pre ,cur = 0 , 1
k = 1

ind = int(input())
if ind == 0 :
    cur = 0
else :
    while k <= (ind-1) :
        pre , cur = cur ,pre + cur
        k += 1


print("the "+str(ind)+"th fubi number is "+str(cur))


    

