s ='abobobefghbobobnmbobplbobob'
bob='bob'
count = 0
i=0

while (i < len(s)-2):
   if ( bob == s[i]+s[i+1]+s[i+2]):
      print s[i]+s[i+1]+s[i+2]
      count+=1
   i += 1

print 'Number of bobs:', count
