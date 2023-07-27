size=int(input('Enter a list Size:'))
arr=[]
arr2=[]
print('enter a list numbers:')
for i in range(0,size):
    arr.append(int(input()))
for i in range(0,size):
        for j in range(i+1,size):
              if arr[i]<arr[j]:
                    arr2.append(arr[j])
                    break
        if arr[i]>arr[j]:
              arr2.append(-1)
arr2.append(-1)
print(arr2)
