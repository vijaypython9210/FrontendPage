import pyautogui as pg
import time
time.sleep(2)
a=["Mental","Lusu","Eruma maadu"]
for j in range(10):
    for i in a:
        pg.write("yei {} Yenna pandra".format(i))
        pg.press('enter')
