#!/usr/bin/python

print "Hello Python"
print " oh dear"

# is for comment

2+3
2.0+3
int(3.0+2)
float(5+3)
'abc'
'3'
fo = 'abcdefg'
str1 = 'abc'
str2 = '3'
str4= 3*str1
str3 = str1+str2
str3[0]
str3[:2]
str3[-1]
str3[0:]
str3[0:2:-1]
pi=3.14159
radius = 5.0
area = pi*radius**2
radius =6.0
len(str4) # length of the string

var1= raw_input('Enter an integer:' )
var = input()

if ( var  == 100 ) : print "Value of expression is 100"

elif (var == 11) : print " Wrong passcode"

else : print " it's ok", float(var)

print "Good bye!"


def fact(n):
	"function is for factorial"
	if (n==0): facts=1;	
	else: facts=n*(n-1);
	return facts;

print fact(3)
