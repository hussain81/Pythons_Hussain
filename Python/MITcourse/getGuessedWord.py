def isWordGuessed(secretWord,letterGuessed):
    sw = secretWord
    lg = letterGuessed
    ns = len(sw)
    ng = len(lg)
    if ns!=ng:
       return False

    if ns == 1 and ng == 1:
       if sw[0]==lg[0]:
          return True
       else:   
          
          return False
 
    seclist = []
    prt = ''
    for i in range(0,ns):
       seclist = seclist + [secretWord[i]]
       

    for i in range(0,ns):
       
       for j in range(0,ng):
          
          if seclist[i]==lg[j]:
             lg.remove(lg[j])
             swp = sw[1:]
             #prt += '_ '
             return isWordGuessed(swp,lg)
          
       
    

secretWord = 'iolpec' 
letterGuessed = [ 'p','o','l','i','c','e']
print isWordGuessed( secretWord,letterGuessed)
