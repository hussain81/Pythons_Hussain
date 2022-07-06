def semordnilap(str1,str2):
    if len(str1)!= len(str2):
       return False
    elif len(str1) == len(str2) and len(str1) == 1:
       return True

    else :
       if str1[0]==str2[-1]:
          #print str2[:-1],str1[1:]
          return semordnilap(str1[1:],str2[:-1])
       else:
          return False





def semordnilapwrapper(str1,str2):
    if len(str1)==1 or len(str2) ==1:
       return False
    if str1==str2:
       return False

    return semordnilap(str1,str2)


print semordinlapwrapper( 'a','a')
