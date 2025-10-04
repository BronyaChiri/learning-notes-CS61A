def Q(p,q):
    def f(name):
        if name == 'p':
            return p
        elif name == 'q':
            return q 
    return f 

def q(x):
    return x('q')

def p(x):
    return x('p')

def Q_add(x,y):
    pn = p(x)*q(y) + p(y)*q(x)
    qn = q(y)*q(x)
    return Q(pn,qn)
def Q_mul(x,y):
    pn = p(x)*p(y)
    qn = q(x)*q(y)
    return Q(pn,qn)

def print_Q(x):
    print("x=",p(x),"/",q(x))

a = Q(3,8)
b = Q(9,107)
c = Q_mul(a,b)
print_Q(c)

