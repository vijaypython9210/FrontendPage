arr=[]
sum=0
size=int(input('Enter a list size'))
print('Enter a list value')
for i in range(0,size):
    arr.append(int(input()))
for i in range(1,size):
    if arr[0]>arr[i]:
        sum+=arr[0]-arr[i]
print(sum)

