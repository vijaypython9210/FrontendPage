arr=[2,7,1,15]
target=int(input('Enter your Target number'))
size=len(arr)
for i in range(size):
    for j in range(i+1,size):
        sum=arr[i]+arr[j]
        if(sum==target):
            print(i,j)
            break
