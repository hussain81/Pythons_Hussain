x = int ( raw_input( 'enter an integer' ) )
ans = 0
while ans**3 < abs(x):
  ans =ans + 1
 print ans
if ans**3 != abs(x) :
  print ( str(x) + ' is not a perfect cube')
else :
  if x<0:
    ans = -ans
  print ( 'cube root of ' + str(x) + ' is ' + str(ans) )

# sqrt of a number

y = int(raw_input('enter an integer:' ))
sqr=0
while sqr**2< y:
  sqr = sqr + 1
if sqr**2 != y:
  print (str(y) + 'is not a perfect square' )

else:
  print ( 'the square root of the number is:', sqr, 'and', -sqr )

