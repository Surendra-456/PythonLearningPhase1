student={'name':'Surendra','age':30, 'courses':['Math','Science','Nepali']}

#accessing the dictionery values
#for all as it is
print(student)
#for particular value
print(student['name'])
#what if key not found use get('key','optionalmessagewhen not exist') default=None
print(student.get('name1','Not Found'))