num = input()
if num < 0:
  isNeg = True
  num = abs(num)
else: 
  isNeg = False
result = " "

if num == 0:
  result = '0'

while num > 0:
  result = str(num % 2) + result
  num = num/2

if isNeg:
  result = '-' + result

print result


x= float(raw_input( 'enter a decimal number between 0 and 1:' ))
p = 0
while ((2**p)*x)%1!=0:
  print('Remainder = ' + str((2**p)*x-int((2**p)*x)))
  p+=1

num1 = int(x*(2**p))

result1 =''
if num1 == 0:
  result1 = '0'
while num1 > 0:
  result1 = str( num1 % 2) + result1
  num1 = num1/2

for i in range(p-len(result1)):
  result1 = '0' + result1

result1 = result1[0:-p] + '.' + result1[-p:]

print (str(result1))
 
