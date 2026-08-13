student={'name':'Surendra','age':30, 'courses':['Math','Science','Nepali']}

#accessing the dictionery values
#for all as it is
print(student)
#for particular value
print(student['name'])
#what if key not found use get('key','optionalmessagewhen not exist') default=None
print(student.get('name1','Not Found'))

#update the value in  dictionery
student.update({'name':'Surendra Pd Nishad','age':35, 'courses':['Math','Science','Nepali','Biology']})
print(student)

#del keyword to delete the specific key
del student['courses']
print(student)

#another way to delete is pop() which will return delete key
s=student.pop('name')
print(student)
print(s)

#to see how many key use len(variable)
print(len(student))

#to see  keys use student.keys()
print(student.keys())

#to see  values use student.values()
print(student.values())

#to see  key and value use student.items()
print(student.items())

#for loop is just like list
for key,value in student.items():
    print(key,value)
