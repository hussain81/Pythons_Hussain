t1 = (1, 'two', 5)
t2 = (t1, 'four')

t3 = ( 'five',)
#print t1+t2        # concatenation
#print (t1+t2)[1:5]
#print t1+t2+t3
t4=()


def finddivisors(n1,n2):
    divisors = ()
    for i in range(1,min(n1,n2)+1):
        if n1%i==0 and n2%i==0:
           divisors = divisors+(i,)
    return divisors

print finddivisors(20,40)

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    
    test = ()
    for i in range(0,len(aTup),1):
      print i,len(aTup)
      if i%2 !=1:
        test= test+(aTup[i],)
    return test

aTup = (1,2,3,4,5,6,7)
print oddTuples(aTup)

