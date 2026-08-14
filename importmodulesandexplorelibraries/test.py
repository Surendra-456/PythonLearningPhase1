
# import sys
# sys.append('C:\Program Files\Python314\Lib\my_module.py')
#import my_module as mm
#from my_module import *
from my_module import find_index as fi, test as tst
import sys
import math #standard librarry
import datetime #standard librarry
import random #standard librarry
import calendar #standard librarry

courses = ['History', 'Math', 'Physics', 'CompSci']


#print(mm.find_index(courses, 'Math'))  # Output: 1
#print(find_index(courses, 'Math'))  # Output: 1

print(fi(courses, 'Math'))  # Output: 1
print(tst)  # Output: Hello, World!

print(sys.path) #here is the path where my machine look for modules 
#Step 1: Check the current script folder
#Step 2: Check the ZIP file python314.zip for my_module.py
#Step 3: Check DLLs for my_module.pyd inside C:\Program Files\Python314\DLLs
#Step 4: Check Standard Library Looks for C:\Program Files\Python314\Lib\my_module.py example import os import random import datetime
#Step 5: Check Python installation root C:\Program Files\Python314
#Step 6: Check site-packages C:\Program Files\Python314\Lib\site-packages\my_module.py this is where module install using pipe import requests import pandas import numpy


ran=random.choice(courses)
print(ran)

dat = datetime.date.today()
print(dat)

rad=math.radians(math.sin(30))
print(rad)

print(calendar.month(2026, 8))
print(calendar.calendar(2026))
print(calendar.isleap(2024))
print(calendar.leapdays(2000, 2025))
print(calendar.weekday(2026, 8, 14))
print(calendar.day_name[4])
print(calendar.month_name[8])
print(calendar.month_abbr[8])

first_week_day = calendar.monthrange(2026, 8)[0]
print(first_week_day)


calendar.setfirstweekday(calendar.SUNDAY)
print(calendar.month(2026, 8))