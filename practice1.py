from re import X


print("Hello world")
print("I have been doing this  ")
print(3+5)
a=3+8
print(a)
i=1
x=2
while i<10:
    x=i+x
    i=i+1
    print(x)
#data type
x=str(3)
y=float(3)
z=int(4)
print("string  ", x, "float  ", y, "int  ", z)
a,b,c=2,3,4
print(c)
# a collection of values
collect1=[500, 300, 150]
m,n,k=collect1
#print(k)

#global and local variables
p="great"
def myfunc():
    p="good "
    print(p+"job")

myfunc()
print(p+"job")

#global keyword
def myfunc1():
    global d
    d ="good "
    print(d +"job")

myfunc1() #you have to call the function to use the global variable from that function
print(d +"health")


