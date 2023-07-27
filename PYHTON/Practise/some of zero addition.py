a=[]
n=int(input())
print('enter the array numbers')
for i in range(n):
    s=int(input())
    a.append(s)
for i in range(0,n):
    for j in range(i+1,n):
        for k in range(i+2,n):
            l=a[i]+a[j]+a[k]           
if(l==0):
    print("Yes")
else:
     print('No numebr adddtion of becomes zero')
