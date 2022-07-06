aStr = "abcdefghijklmnopqrsyz"



def isIn(char,aStr):

   if aStr == "":
      return False

   elif len(aStr)==1:

      if len(char)==1 and char==aStr:
           return True
      else:
           return False

   elif len(aStr)>1:
      n = len(aStr)/2     
      if char == aStr[n]:
          print aStr[n]
          return True
      else:
          n = len(aStr)/2
          if char > aStr[n]:
             return isIn(char, aStr[n:])

          elif char < aStr[n]:
             return isIn(char, aStr[:n])
                 

char = 'u'

print isIn( char, aStr)
