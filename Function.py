def factorials(n):
     
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
    
print(factorials(1), factorials(-3), factorials(5))


# lambda function: can take any number of arguments but can only be a single expression
x=lambda a,b,c : a**2+b+c
y=lambda x,y,z : x+x*y-z**2+5*x
#print(y(2,5,1))
