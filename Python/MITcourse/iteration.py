x=3
ans = 0
itersleft = x
while ( itersleft !=0 ):
  ans = ans + x
  itersleft = itersleft - 1

print(str(x) + " * " + str(x) + ' = ' + str(ans))

num = 10
while True:
    if num < 7:
        print 'Breaking out of loop'
        break
    print num
    num -= 1
print 'Outside of loop' 

# in while loop if there is any break statement that actually terminates the loop 
# while true means as long as the state men is true it will continue going through the loop.

