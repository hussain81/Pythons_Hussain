x = int ( raw_input( 'enter an integer' ) )
for ans in range(0,abs(x)+1):
  if ans**3 == abs(x) :
     break
if ans**3!=abs(x):
     print ( str(x) + ' is not a perfect cube')
else :
     if x<0:
       ans = -ans
     print ( 'cube root of ' + str(x) + ' is ' + str(ans) )


school = 'Massachusetts Institute of Technology'
numVowels = 0
numCons = 0

for char in school:
    if char == 'a' or char == 'e' or char == 'i' \
       or char == 'o' or char == 'u':
        numVowels += 1
    elif char == 'o' or char == 'M':
        print char
    else:
        numCons -= 1
        print char, numCons

print 'numVowels is: ' + str(numVowels)
print 'numCons is: ' + str(numCons) 


