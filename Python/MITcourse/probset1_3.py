#s ='abcdefamnopqmbobplbobob'
s= 'bzxcb'

substr=""
result=s[0]

for i in range(len(s)): 
    if s[i-1]<=s[i]:
       substr +=s[i]
       if (len(substr)>len(result)):
          result = substr
    else:
       substr = s[i]  
print 'Longest substring in alphabetical order is:', result


