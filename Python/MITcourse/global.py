def fibmetered(x):
   global numcalls
   numcalls +=1
   if x==0 or x==1:
      return 1
   else:
      return fibmetered(x-1) + fibmetered(x-2)


def testFib(n):
   for i in range(n+1):
      global numcalls
      
      numcalls=0
      
      print ( 'fib of' + str(i) + '=' + str(fibmetered(i)))
      print numcalls

testFib(5)
