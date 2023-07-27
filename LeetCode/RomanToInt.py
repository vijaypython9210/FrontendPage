roman={'I':1,'V':5,'X':10,'L':50,'C':100,"D":500,'M':1000}
sum=0
user_input=input('Enter a Roman Letter Number:')
for i in user_input:
    if (i in roman):
        sum+=int(roman[i])
    else:
        print('enter a valid roman letter')
        sum=0
        break
print(sum)