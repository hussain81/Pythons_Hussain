def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)

def radiationExposure(start,stop,step):
    n = int((stop-start)/step)
    listy=[]
    
    for i in range(0,n+1):
       listy += [f(start+i*step)*step]
    listx=listy[:]
    #print listy[:]
    ans = 0.0
    for i in range(0,n):
       ans = ans + listx[i]
       #print i, ans
    return ans

print radiationExposure( 5,11,1)
