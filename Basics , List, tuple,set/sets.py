#difference between set ,tuple ,list are
course_set1= {'Math','Science','English','Nepal'}
print(course_set1)

#PS C:\Python> python sets.py 
#{'English', 'Math', 'Science', 'Nepal'}
#PS C:\Python> python sets.py
#{'Math', 'Science', 'Nepal', 'English'}
#PS C:\Python> python sets.py
#{'English', 'Nepal', 'Math', 'Science'}

#Note: The order of elements in a set is not guaranteed to be the same every time you print it. Sets are unordered collections, so the order of elements may vary each time you run the code.

course_setA= {'Math','Science','English','Nepal','Math'}
course_setB= {'Math','Science','English','Nepal'}
course_setC= {'Physics','Biology','Nepal'}

print("Math" in course_setA)
#duplicate records not show in print
print("Remove 'Math ' which is duplicate records",course_setA)
#shows common 
print("Common is:",course_setB.intersection(course_setC))
#shows difference
print("difference is:",course_setB.difference(course_setC))
#shows union
print("union is:",course_setB.union(course_setC))

#Note for creating empty
#list
li=[]
li2=list()
#tuple
tu=()
tu2=tuple()
#set
se=set();