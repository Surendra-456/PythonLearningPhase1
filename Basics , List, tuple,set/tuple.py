#tuple () is immutable data type which means we can not change the value of tuple once it is created
course_tuple1= ('Math','Science','English','Nepal')
course_tuple2=course_tuple1
print(course_tuple1)
print(course_tuple2)

course_tuple2[0]= 'Algebra'
print(course_tuple1)
print(course_tuple2)

('Math', 'Science', 'English', 'Nepal')
('Math', 'Science', 'English', 'Nepal')
#Traceback (most recent call last):
 # File "C:\Python\tuple.py", line 7, in <module>
 #   course_tuple2[0]= 'Algebra'
#TypeError: 'tuple' object does not support item assignment