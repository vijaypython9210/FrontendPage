list=[1,2,3,4,5]

pos1=int(input("Enter a pos1:"))
pos2=int(input("Enter a pos2"))

# temp=list[pos1]
# list[pos1]=list[pos2]     Genreal Method
# list[pos2]=temp

list[pos1],list[pos2]=list[pos2],list[pos1]

print(list)