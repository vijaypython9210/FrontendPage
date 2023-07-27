'''
one="good"
two="man"
three=f" {one} {two}"
print (three)

four=three.title()
print(four)

five=three.upper()
print(five)

six=three.lower()
print(six)

seven=f"hello,{five}.title()"
print(seven)

eight=three.lstrip()            #remove the white space in left
print(eight)

three1="Good morning msg!"
print(three1)

nine=three1.rstrip()            #remove the whitesapce in right side
print(nine)

ten=three.strip()               #remove the whitespace in both sides
print(ten)
'''
aa=['Pen','Color','Paper','books','Exam']
print(aa)

ab=aa[0]
print(ab)
print(aa[3].title())

aa[0]='Pencil'
print(aa)

aa.append('Notes')
aa.append('class')
print(aa)

aa.insert(2,'Ink')
print(aa)

del aa[2]
print(aa)

ac=aa.pop()
ad=aa.pop(0)
print(ac)
print(ad)
print(aa)

aa.sort()                               #Alphabet Arrangement
print(aa)

aa.sort(reverse=True)           #Reverse Alphabet Arrangement
print(aa)
