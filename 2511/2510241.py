def min_index(listx):
    min_x = min(map(abs,listx))
    l = [i for i in range(len(listx)) if abs(listx[i])== min_x]
    return l

a = [5,2,3,-2,-7,-9,3,4]

def adjcent_max(listx):
    l1 = listx[1:]
    l2 = listx[:-1]
    added = [a + b for a,b in zip(l1,l2)]
    added2 = [listx[i]+listx[i+1] for i in range(len(listx)-1)]
    return added2,added
    
def dic_end(listx):
    t = list(map(abs,listx))
    dic = {end:[i for i in t if i%10==end] for end in range(10) if any([x%10==end for x in t])}
    return dic



print(dic_end(a))
