input= int(input("Enter the number for factor find:"))
fact=1
for i in range(input,0,-1):
    fact*=i
print(fact)