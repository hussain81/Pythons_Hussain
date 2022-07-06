balance = 32000
annualInterestRate = 0.2

air = annualInterestRate
mir = air/12.0

numguess=0

low = balance/12.0
high = (balance*(1.0+mir)**12)/12.0

minpay = (low+high)/2.0
rembal = balance
nmonths = 1
while ( abs(rembal-minpay) >=0.001 ):
  rembal = balance
  numguess+=1
  for nmonths in range(1,12):

    newbal = rembal - minpay
    rembal = newbal + mir*newbal
    #print 'Remaining balance: ',rembal,nmonths,minpay
      
  if( minpay< rembal):
    low = minpay
  else:
    high = minpay
  
  minpay =(low+high)/2.0
  #print minpay
print 'Lowest Payment: ',round(minpay,2)
#print numguess   

