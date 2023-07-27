arr=[3,4,6,7,5]
size=int(len(arr))-1
for i in range(1,size):
    if(arr[i-1]<arr[i] and arr[i+1]<arr[i]):
        print(arr[i]," is peak Number")
