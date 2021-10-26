import time
from shortcuts import clearScreen

num = int(input('Welk nummer wilt u de tafel van?\n'))
clearScreen(0.5)
for i in range(1,11):print(num * i);time.sleep(0.25)