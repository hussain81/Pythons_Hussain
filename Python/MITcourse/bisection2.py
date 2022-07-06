low = 0
high = 100
guess = (high+low)/2
print 'Please think of a number between 0 and 100!'

check = str
while (check!= 'c') :
 print( ' Is your secret number ', guess, '?'\
 'Enter', 'h', 'to indicate the guess is too high','.',\
 'Enter', 'l', 'to indicate the guess is too low','Enter', 'c', \
 'to indicate I guessed correctly')
 urresponse = str(raw_input())
 check = urresponse 
 if check == 'h':
      high=guess
      guess = (low+high)/2
 elif check == 'l':
      low = guess
      guess = (high+low)/2
 elif check != 'c':
      print ('Sorry, I did not understand your input.')
      guess = (high+low)/2

print ( 'Game over.', 'your secret number was: ' , guess)  
