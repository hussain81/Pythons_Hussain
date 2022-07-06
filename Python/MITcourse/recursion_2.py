def gcdrecur(a,b):
  if a == 0:
    return b
  elif b == 0:
    return a
  elif a>b :
    return gcdrecur(b,a%b)
  else :
    return gcdrecur(a,b%a)

print gcdrecur(124,72)

# simpler is
def gcdRecur(a,b):
   if b==0:
      return a
   return gcdRecur(b,a%b)

    
