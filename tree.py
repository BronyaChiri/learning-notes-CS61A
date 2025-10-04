from functools import lru_cache

def tree(label,branches=[]):
    for b in branches:
        assert is_tree(b), 'branches must be trees'
    return [label]+list(branches)

def is_tree(t):
    if type(t) != list or len(t) < 1:
        return False
    for b in branches(t):
        if not is_tree(b):
            return False
    return True
    
def branches(t):
    return t[1:]

def label(t):
    return t[0]

def is_leaf(t):
    return len(branches(t)) == 0 

@lru_cache(maxsize = 1024)
def fib(n):
    if n <= 1:
        return tree(n)
    else:
        left , right = fib(n-2) , fib(n-1)
        return tree(label(left)+label(right),[left,right])
    
def count_leaves(t):
    if is_leaf(t):
        return 1
    else:
        return sum([count_leaves(b) for b in branches(t)])
    


def leaves(t):
    if is_leaf(t):
        return [label(t)]
    else:
        return sum([leaves(b) for b in branches(t)],[])
    

