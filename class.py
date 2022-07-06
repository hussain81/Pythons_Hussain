import math
class myclass1:
    x=3
    y=5
    z=x+y

#create an object
obj1=myclass1()

print(obj1.x, " ", obj1.z, "  " , myclass1.y)

# _init_() Function

'''
class genPhys:
    def __init__(self,j,k):
        self.j=j
        self.k=k
obj2=genPhys(4,5)
print(obj2.j)
'''
class genPhys2:
    def __init__(self,x,y):
        a=24
        b=34
        self.x=x+a+b
        self.y=y-a-b+2*self.x
        self.y=self.y*2
    def func1(abc):
        return abc.y
obj3=genPhys2(11, 99)
print(obj3.y)
print(obj3.func1())
#empty class
class myfunc1:
    pass

