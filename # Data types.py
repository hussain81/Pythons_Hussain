# Data types
x="hello" #str
y=3 #int
z=6.0 #float
a= 3+1j #complex
#print((a))
F=[1,2,6] #list, only same data types
D=(2,3,"string") #tuple- can have different data types
#print(D)
c=range(1,20,3) # range of values range(start,stop, step size)
for n in c:
    print(n)
J=dict(name="John", age=36)
#print(J)
B=bool(5)
# using the types, int, float, complex the types can be changed
a=15.36
b=23
c=2e5    # e means 10^power
print(int(a), float(b), complex(a), c)

import random
print(random.randrange(5,10))

