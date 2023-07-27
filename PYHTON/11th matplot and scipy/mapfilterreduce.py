#                                     MAP
# student=[('maths','anitha',180),('biology','anand',180),('biology','balaji',170),('maths','chandru',190)]
# stu_mark=lambda item:(item[0],item[1],float('{:.2f}'.format(item[2]/100)))
# stu_per=list(map(stu_mark,student))
# print(stu_per)
# stu_mark1=lambda item:(item[1],int(item[2]/2)) 
# stu_per1=list(map(stu_mark1,student))
# print(stu_per1)

# val=[72,78,99,12,56]
# val_check=lambda x:"even" if x%2==0 else "odd"
# val_map=list(map(val_check,val))
# print(val_map)

# temp=[102,99,89,70,103]
# temp_check=lambda x:float('{:.2f}'.format((x-32)*(5/9)))
# temp_map=list(map(temp_check,temp))
# print(temp_map)


#                                   FILTER
# items=[(3456,'shoes',780),(3566,'phone',25300),(2587,'book',450),(5412,'pen',72)]
# item_number=lambda item:3000<item[0]<5000
# item_filter=list(filter(item_number,items))
# print(item_filter)

# student=[('maths','anitha',180),('biology','anand',180),('biology','balaji',170),('maths','chandru',190)]
# stu_name=list(filter(lambda x:x[1][0]=='a',student))
# print(stu_name)
# stu_mark=list(filter(lambda x:x[2]>=180,student))
# print(stu_mark)

#                                       REDUCE
import functools                                       
val=[10,20,30,40,50]
val_add=functools.reduce(lambda x,y:x+y,val)
print(val_add)

name=['V','I','J','A','Y']
print(functools.reduce(lambda x,y:x+y,name))