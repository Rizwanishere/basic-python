# import random

# import pyautogui as pg

# import time

# yo=('waste','hopeless','fat')

# time.sleep(8)

# for i in range(10):
#     a=random.choice(yo)
#     pg.write("You Are "+a)
#     pg.press('enter')


import pyautogui
import time

time.sleep(4)

# for i in range(20):
#     pg.write("assalamualaikum")
#     pg.press('enter')
count=1


while count<=20:
    pyautogui.typewrite("assalamualaikum "+str(count))
    pyautogui.press("enter")
    count=count+1