balance = 4773.0
annualInterestRate = 0.2

air = annualInterestRate
mir = air/12.0



minpay = 0
while ( minpay < balance ):
  
  rembal = balance  
  nmonths=1
  while (nmonths <=12):

    newbal = rembal - minpay
    rembal = newbal + mir*newbal
    
    #print 'Remaining balance: ',rembal,nmonths,minpay
    nmonths +=1
  if( rembal<0.01):
    break
  minpay +=10
  #print minpay
    
   
print 'Lowest Payment: ',round(minpay,2)

