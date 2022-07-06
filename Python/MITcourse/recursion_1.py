

def mult(a,b):
   result = 0
   while ( b>0):
     
     result += a
     b-=1
   return result


def recurmul(a,b):
   if ( b==1):
     result = a
     return result
   else:
     result = a+recurmul(a,b-1)
   return result

print recurmul(2,5)

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    
    result=1.0
    while( exp >0):
      result = base*result  
      exp -= 1
    return result

print iterPower(8.96,4)
