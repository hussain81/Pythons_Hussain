x=25
epsilon = 0.01
numguesses=0
low = 0.0
high =x
ans=(high+low)/2.0

while abs(ans**2 - x) >= epsilon:
  print( 'low = ' +str(low) + ' high = ' + str(high) +'ans = ' + str(ans))
  print(low, '----', high)
  numguesses +=1
  if ans**2 < x: 
    low = ans
  else:
    high = ans
  ans = (high+low)/2.0

print ( 'numguesses: ' , str(numguesses))
print ( str(ans) + 'is close to square root of' + str(x))
