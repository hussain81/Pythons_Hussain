print 'username: must not be less than 5 characters'
user= str(raw_input())
x = user.upper();
print 'password'
password = str(raw_input( ))

varA = 'aba'
vary= 123

#if type(user) == type(varA) and type(password) == type(vary):
 # print 'logged in' 
#else:
  #print 'incorrect password'

if len(user)<5 and len(password)<5:
  print 'incorrect username and password'
elif len(user) < 5 :
  print 'incorrect username'
elif len(password) < 5 :
  print 'incorrect password'
else:
 print x, 'logged in'

print '5'>'a';
