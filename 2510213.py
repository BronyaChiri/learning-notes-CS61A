class reasonable:
    def __init__(self,n,d):
        self.numer = n
        self.domin = d
    
    def __float__(self):
        return self.numer/self.domin
    
    def __add__(self,other):
        return float(self) - float(other)  #very strange ,yah!
    
    __radd__ = __add__

a = reasonable(3,8)
b = reasonable(3,7)

print(a+b,b+a,float(a))
    
