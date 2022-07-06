
x = int(raw_input('enter an integer:' ))
y = raw_input()

if x%2 == 0 :   
  if x%3==0:
    print('divisible by 2 and 3 ')
  else: 
    print( 'divisible by 2 only' )
elif x%3 == 0:      
  print('divisible by 3 only not 2') 
else : 
  print( ' not divisible by 2 and 3')


if x>y :
  print ( 'x is bigger' )
else :
  print ( 'y might be bigger' )
print('done with conditional')
