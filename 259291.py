from functools import lru_cache
values = [1,3,1,4,1,5,9,14]
target = 9
'''
multisum = []
minsum = 0 

class angle():
    def __init__(self,lst,havsum):
        self.lst = lst
        self.havsum = havsum 

    def calsum(lst):
        if len(lst) == 3:
            return lst[0]*lst[1]*lst[2]
        else:
            for i in range(len(lst)):
                nv_1 = [m for m in lst if m != lst[i]]
                multisum[i] = lst[i-1]*lst[i]*lst[i+1]




print(calsum(values))
 '''
'''
@lru_cache(maxsize = 256)
def decouple(i,j):
    if j - i <=1 :
        return 0
    elif j - i == 2:
        return values[i]*values[i+1]*values[i+2]
    else:
        return min((values[i]*values[k]*values[j]+decouple(k,j)+decouple(i,k))for k in range(i+1,j))
    
print(decouple(0,len(values)-1))
'''
'''
hashtable = dict()
for i,num in enumerate(values):
    hashtable[num] = i
    if target - num in hashtable:
        if i != hashtable[target - num ]:

            print([i,hashtable[target - num]])


'''


def trasfer(linkl):
            while linkl:
                t.append(linkl.val)
                linkl = linkl.next
            return t

def trans(lis):
            for i in lis:
                wh = ListNode(i,wh.next)
              
            return wh 
def couple(l):
            num = 0
            for i,t in enumerate(l) :
                num += t * (10**i)
            return num 
        
def decouple(x):
            
            
            nl , last , i = x , x%10 , 0
            while nl >= 10:
                
                nl , last = nl // 10 , nl % 10
                a[i] = last
                i += 1

            return a 

print(trans(decouple(couple(transfer(l1))+couple(transfer(l2)))))
        

        
