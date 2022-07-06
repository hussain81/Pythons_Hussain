import math

pi=math.pi

def fact(n):
     
    if n==0 or n==1:
        return 1
    elif n>1:
        i=1
        x=n
        while i<n:
            x=x*(n-i)
            i=i+1
        return x
    else:
        return 0

def comb(n,r):
    if r<=n:
        return fact(n)/(fact(r)*fact(n-r))
    else:
        return 0
    
print (comb(5,3))

