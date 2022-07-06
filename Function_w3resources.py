#*******************************************
def maxof3(x,y,z):
    if x>y and x>z:
        print(x)
    elif z>y and z>x:
        print(z)
    elif y>x and y>z:
        print (y)
    elif x==y and x>z:
        print(x)
    elif x==z and x>y:
        print(x)
    elif y==z and y>x:
        print(y) 


maxof3(24,34,34)

#***************************************    

def sumall(x):
    i=0
    sum=0
    while i < len(x):
        sum=sum+x[i]
        i=i+1
    return sum

a=[1,5,12,10]
#print(len(a),a[1])
#print(sumall(a))
#***************************************
def multiplyall(x):
    i=0
    sum=1
    while i < len(x):
        sum=sum*x[i]
        i=i+1
    return sum
#print(multiplyall(a))
#***************************************
# def reverse_string(x):
#     n=len(x)
#     i=0
#     result=""
#     while i< n:
#         result=result+x[n-i-1]
#         i=i+1
#     return result
# str1="I live in Dhaka"
# print(reverse_string(str1))
#***************************************
# def is_upper_or_lower(x):
#     i=0
#     n=0
#     m=0
#     while i<len(x):
#         a=x[i]
#         if a.isupper()==True:
#             n=n+1
#         elif a.islower()==True:
#             m=m+1
#         i=i+1
#     print(n, "upper case letters ", m, "lower case letters " )
# s=" The Quick Brown Fox "
#is_upper_or_lower(s)
#**************************************************

# def unique_list(x):
#     i=0
#     while i<len(x):
#         j=i
#         if x[i]==x[j+1]:
#             a=x[i+1]
#             x.remove(a)
#             j=j+1
#             print(a)
#         else:
#             i=i+1
#     return x
# x=[1,1,3,4,4,4,4,5]
# print(unique_list(x))

def unique_list1(x):
    y=list(dict.fromkeys(x))
    return y
a=[1,1,3,4,4,5,5]
print(unique_list1(a))

