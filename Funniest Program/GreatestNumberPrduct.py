arr=[]
product=1
count=0
size=int(input('Enter a list size'))
print('Enter a list value')
for i in range(0,size):
    arr.append(int(input()))
for i in range(0,size):
    if arr[i]==0:
        break
    elif arr[i]<0:
        count+=1
        index=i
if count%2==0:
    for i in range(0,)
            