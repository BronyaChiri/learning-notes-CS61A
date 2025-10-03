"""def fib(x):
    if x == 0:
        return 0 
    elif x == 1:
        return 1
    else:
        return fib(x-1) +fib(x-2)
    
print(fib(43))
""" '''
def part(x,y):
    if y == 1 :
        return 1 
    elif x ==0:
        return 1
    
    elif x < 0 or y <= 0  :
        return 0 

    else:
        return part(x-y,y) +part(x,y-1)
    
print(part(100,13))
'''
'''elif x <=y :
        return part(x,x-1)'''
'''
class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
  ''''''
rec = Rectangle(15,15)
print(rec.area())
'''
nums = [2,1,2]

def judge(x, y, z):
            m = max(x, y, z)
            if (x + y + z) >= 2 * m:
                return True
            else:
                return False
class Solution:
    def __init__(self,nums = nums):
        self.nums = nums
    

    def search(self):
        done = 0
        S_max = 0
        for i in self.nums:
            done += 1

            for t in self.nums[done:]:
                for k in self.nums[done + 1 :]:
                    if judge(i, t, k):
                        if (i + t + k) >= S_max:
                            S_max = i + t + k
        print(S_max)
        return S_max
a = Solution()  
print(a.search())
