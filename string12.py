
# for long string use three double quotes or single quotes
xx="""here is the long string one can try"""
print(xx)
print(len(xx))
print(xx[5])
# reading from the end of the string by using negative index
print(xx[-20:-1])
print(xx.lower()) # lower case
print(xx.upper()) # upper case
#changing format
itemnumber=200
storenumber=1560
k="get {} items from walmart store number {}"
print(k.format(itemnumber,storenumber))
