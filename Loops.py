C=range(1,50,5)
for n in C:
    print(n)
#while loop
i=0
while i<50:
    i=i+5
    if i==35:
        break   #break means stopping the iteration loop
    print(i+10)
#else if
a=50
b=7
if b>a:
    b=b+a
    print(b)
elif b==a: 
    b=b*a
    print(b)
else:
    print(b)
