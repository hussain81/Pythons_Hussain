varA = input()
varB = input()

var = 'abac'

if type(varA) == type(var) or type(varB) == type(var):
  print 'string involved'
elif varA > varB:
  print 'bigger'
elif varA == varB:
  print 'equal'
else:
  print 'smaller'
