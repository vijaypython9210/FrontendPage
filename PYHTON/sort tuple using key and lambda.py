# student=[('maths','anitha',80),('biology','anand',80),('biology','balaji',70),('maths','chandru',90)]
# student.sort()
# print(student)
# student.sort(key=lambda item:item[2])
# print(student)
# student.sort(key=lambda item:item[1])
# print(student)
# student.sort(key=lambda item:item[1],reverse=True)
# print(student)

student=(('maths','anitha',80),('biology','anand',80),('biology','balaji',70),('maths','chandru',90))
print(sorted(student))
print(student)
print(sorted(student,key= lambda item:item[2]))