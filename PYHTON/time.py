import time
'''t=time.sleep(2.5)
print(t)'''


t=time.localtime(1650111319.6595328)

r=time.mktime(t)
print(r)

m=(2020, 4, 3, 8, 44, 4, 50, 362, 0)
s=time.asctime(m)
print(s)

z=time.localtime()
print(z)
print(z.tm_hour)
print(z.tm_zone)

c=time.strftime("%a,%m/%d/%Y, %H:%M:%S",z)
print(c)

n="21 June,2029"
d=time.strptime(n,"%d %B,%Y")
print(d)

