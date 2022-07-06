tech = ['MIT', 'Cal Tech']
Ivys = ['Harvard', 'Yale', 'Brown']
univs = [tech,Ivys]
tech1 = [1]
#print tech+Ivys
tech.append('RIP')
#print univs


#for e in univs:
#   print 'elements ', e
 #  for u in e:
  #    print u

flat = tech + Ivys
print flat

def removedups(L1,L2):
   L1start = L1[:]
   for e1 in L1start:
      if e1 in L2:
        L1.remove(e1)

L1 = [1,2,3,4,5]
L2 = [1,2,3,6,7]

removedups(L1,L2)
print L1


a = [1,7,8,3,0,9]
a.sort()
print a
