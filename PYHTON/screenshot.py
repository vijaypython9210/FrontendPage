import pyautogui as pg
import time
for i in range(100):
    screenshot = pg.screenshot()
    screenshot.save("ss[i].png")                                                 
    time.sleep(3)
