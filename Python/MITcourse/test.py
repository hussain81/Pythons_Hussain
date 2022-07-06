x=5
def f(x):
  fc = x**2;
  return fc;

#x = int (raw_input());

print f(x);

def g(x):
  fc = x**3;
  return fc;

print g(6);

def fact(n):
  "function is for factorial"
  if (n==0): 
     facts=1;	
  else: 
     facts=n*fact(n-1);
  return facts;

print fact(6)
