x = float(raw_input('enter a number:' ))
p = int(raw_input('enter a integer power: ' ))

result = 1
for turn in range(p):
  print( 'iteration: '+ str(turn) + 'current result:' + str(result))
  result = result*x 
print result
