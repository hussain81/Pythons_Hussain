def getRatios(v1,v2):
    ratios = []
    for index in range(len(v1)):
       try:
           ratios.append(v1[index]/float(v2[index]))
       except ZeroDivisionError:
           ratios.append(float('NaN'))
       except:
           raise ValueError('getRatios called with bad arguments')
    return ratios


try:
    print getRatios([1,4,7],[3,0,6])
    print getRatios([],[])
    print getRatios([1,3,9],[1,2])
except ValueError, msg:
    print msg
    
#print getRatios([1,4,7],[0,9,4])
