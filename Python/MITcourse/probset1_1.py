s ='abacdefghi'
vow = 'aeiou'
count = 0
i=0

while (i < len(s)):
  j=0
  while( j < len(vow)):
    if ( vow[j] == s[i]):
      #print s[i]
      count+=1
    j+=1
  i=i+1

print 'Number of vowels:', count
