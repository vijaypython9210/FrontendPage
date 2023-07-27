list=[12,35,9,54,24]
size=len(list)
first,last=list[0],list[size-1]
list[0]=last
list[size-1]=first

print(list)