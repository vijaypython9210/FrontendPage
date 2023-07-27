sub1=int(input("enter the marks of first subject"))
sub2=int(input("enter the marks of secong subject"))
sub3=int(input("enter the marks of third subject"))

tot=sub1+sub2+sub3
per=float((tot*100)/300)

print( "mark1:",sub1)
print("mark2:",sub2)
print( "mark3:",sub3)
print( "total:",tot)
print( "percentage:",per)

if(per>=80):
    print ("grade: A")
elif((per>=70) and (per<80)):
    print ("grade: B")
elif((per>=60) and (per<70)):
    print ("grade: C")
elif((per>=40) and (per<60)):
    print ("grade: D")
else:
    print ("grade: E")
