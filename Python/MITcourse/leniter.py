s='abcfdretyuasdaaaa'
## ############### recursive hard way #####
def leniter(s):
    i=0
    def length(s,i):
      x = s[0]
      
      if s==x:
         return i+1
      else: 
         
         return length(s[1:],i+1)
    return length(s,i) 

print 'length of a string:', leniter(s)


aStr ='abc'

## ############### iterative easy way ######

def leniterr(aStr):
   count = 0
   for char in aStr:
     count +=1

   return count
print leniterr(aStr)


## ############### iterative hard way ########
def lenIter(aStr):
  if aStr == '':
      return 0
  else: 
      x=aStr[-1]
      i=0
      bstr=aStr
      while (i>=0):
     
        bstr = aStr[i:]
        if ( bstr==x):
           break
        i+=1
     
      return i+1
   
print lenIter(aStr)



## ############### recursive easy way##############
def lenRecur(aStr):
       if aStr == '':
          return 0
       else:
          return 1+lenRecur(aStr[1:])

print lenRecur(aStr)
     

   
