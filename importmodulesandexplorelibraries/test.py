#import my_module as mm
from my_module import find_index as fi, test as tst

courses = ['History', 'Math', 'Physics', 'CompSci']


#print(mm.find_index(courses, 'Math'))  # Output: 1

print(fi(courses, 'Math'))  # Output: 1
print(tst)  # Output: Hello, World!