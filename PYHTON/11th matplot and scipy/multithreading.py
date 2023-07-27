import threading
import time

def update_db():
    print("Db processing.....")
    time.sleep(5)
    print("Db Updated")

def display_num(num):
    for i in range(1,num+1):
        print(i)
    
thread_new=threading.Thread(target=update_db)
thread_new.start()

display_num(50)

print(threading.active_count())
print(threading.enumerate())

thread_new.join()
print("Bye")