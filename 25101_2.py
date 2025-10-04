from tree import *

def print_tree(t,indent = 0):
    print(' '*indent + str(label(t)))
    for b in branches(t):
        print_tree(b,indent+1)

def line_sum(t,so_far=0):
    if is_leaf(t):
        so_far += label(t)
        return so_far
    else:
        so_far += label(t)
        for b in branches(t):
            line_sum(b,so_far)

def meet_nbr(t,n):
    if is_leaf(t):
        if label(t) == n:
            return 1
    else:
        for b in branches(t):
            if line_sum(b) == n:
                return 1

tr = fib(4)
print(meet_nbr(tr,7))





#print_tree(tr)
#line_sum(tr,0)
