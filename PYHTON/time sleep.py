import time
import threading 
'''print("Hello boy")
t=time.sleep(2.5)
print("Hello guys how are you?")'''

'''while (True):
    s=time.localtime()
    v=time.strftime("%H:%M:%S %p",s)
   # print(v)
    print(v,end=" ",flush=True)
    print('\r',end=" ",flush=True)
    time.sleep(2)'''
#MULTI THEARDING

def hello():
    for i in range(3):
         print("Hello")
         time.sleep(1)

def hi():
    for i in range(3):
        print("Hi")
        time.sleep(1)

t1=threading.Thread(target=hello())
t2=threading.Thread(target=hi())
t1.start()
t2.start()
