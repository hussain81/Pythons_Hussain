s= 'abchugijkl'
letters = len(s)
ans = 0
start = 0
endincrement = 2
startincrement = 0
x = len(str(s)) - 1
y = str(s)[0:2]
count1 = 0
str1 = ''
if len(s) == 1:
    print('Longest substring in alphabetical order is: ' + str(s))
elif len(s) > 1: 
    while len(y) >= 2:
        if len(y) < 2:
            break    
        elif (start + 1) == len(y):
            break
        elif y[start] < y[start+1]:
            endincrement += 1
            start += 1
            if len(y) > len(str1):
                str1 = y        
            y = str(s)[startincrement:endincrement]

        elif y[start] > y[start+1]:
            if len(y) < 2:
                break
            startincrement += 1
            endincrement = startincrement + 2
            start = 0
            y = str(s)[startincrement:endincrement]

    print('Longest substring in alphabetical order is: ' + str1)




s = 'abcdefghsich'
count = 1
string1 = ""
result = ""
for char in s:
if count != len(s) + 1:

    if ord(char) < ord(s[count]):

        string1 = string1 + str(char)

        count += 1


    else:
        result = result + str(char)
        count += 1
if len(string1) < len(result):
         string1 = result

         result = ''
print string1

