list=['Gfg','is','best','for','Geeks']

list1=list[:]           #coping a list 

res=[sub.replace('G','_').replace('e','G').replace('_','e') for sub in list]
print(res)
print(list1)