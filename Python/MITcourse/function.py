#!/usr/bin/python

# if import state ment is "import circle", to read the variables or functions 
#from the file will be " circle.area(2), circle.pi and so on"

#import circle
#print circle.area(2)


# if import statement is like " from circle import*" it means import all the 
# things from the file. But if we define anything of same name after 
# importing the file it will take the later value.

pi = 1.0

from circle import*
print pi

def fact(n):
  "function is for factorial"
  if (n==0): 
     facts=1;	
  else: 
     facts=n*(n-1);
  return facts;

#print fact(3)

def iterativepower(x,p):

  result = 1
  for turn in range(p):
    print( 'iteration: '+ str(turn) + 'current result:' + str(result))
    result = result*x 
  return result


