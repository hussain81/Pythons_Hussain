


def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if a<b:
      if b%a == 0:
        return a
      else:
        
        i=a-1
        gcd =1
        while (i >0):
          #print i,float(b)/i , float(a)/i
          if ( a%i == 0 and b%i == 0):
            gcd = i
            break
          else:
            gcd = 1
          i-=1 
         
        return gcd
        
        
    elif a>b :
      if a%b == 0:
        return b
      else:
        i=b-1
        gcd =1
        while (i >0):
          print i,float(b)/i , float(a)/i
          if ( a%i == 0 and b%i == 0):
            gcd = i
            break
          else:
            gcd = 1
          i-=1 
        return gcd
    
    elif a==b:
      return a
      
     
print gcdIter(24,212)





def gcdIter1(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''

    if a == b :
      return a

    elif a>b and a%b == 0:
      return b
         
    elif a<b and b%a == 0:
      return a
    
    else:
        i=min(a,b)-1
        gcd =1
        while (i >0):
          #print i,float(b)/i , float(a)/i
          if ( a%i == 0 and b%i == 0):
            gcd = i
            break
          else:
            gcd = 1
          i-=1 
         
        return gcd
        
        
      
     
print gcdIter1(24,212)
