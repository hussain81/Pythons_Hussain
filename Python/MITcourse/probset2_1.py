balance = 5000.0
annualInterestRate = 0.18
monthlyPaymentRate = 0.02

mpr = monthlyPaymentRate
air = annualInterestRate
mir = air/12.0
nmonths=1
rembal = balance
totpaid=0.0
while (nmonths <=12):
 
  minpay = mpr*rembal 
  newbal = rembal - minpay
  rembal = newbal + mir*newbal
  totpaid = totpaid + minpay
  
  print 'Month: ', nmonths 
  print 'Minimum monthly payment: ',round(minpay,2)
  print 'Remaining balance: ', round(rembal,2)
  nmonths +=1

print 'Total paid: ',round(totpaid,2)
print 'Remaining balance: ', round(rembal,2) 

