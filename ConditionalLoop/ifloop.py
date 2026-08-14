# Comparisons:
# Equal:              ==
# Not Equal:          !=
# Greater Than:       >
# Less Than:          <
# Greater or Equal:   >=
# Less or Equal:      <=
# Object Identity:    is
#and
#or
#not

language = 'java'

if language.lower() == 'python':
    print('Language is Python')
elif language.lower()=='java':
    print('Language is Java')
else:
    print('No match')

user='Admin'
isLoggedIn=True
#and
if user.lower()=='admin' and isLoggedIn==True:
    print("Log In Successful!")
elif user.lower()=='' and isLoggedIn==False:
    print("All fields are required!")
else:
    print("Invalid Credential!")


#or
if user.lower()=='admin' or isLoggedIn==True:
    print("Log In Successful!")
elif user.lower()=='' or isLoggedIn==False:
    print("All fields are required!")
else:
    print("Invalid Credential!")

#not
if not user.lower()=='admin':
    print("Invalid Credential!")
elif not isLoggedIn==True:
    print("Unable to login!")
else:       
    print("Log In Successful!")


#In Python, is is a keyword used to check whether two variables refer to the same object in memory. each object has id
a=[1,4,5]
b=[1,4,5]
c=b

print(id(a))
print(id(b))
print(id(c))
# 2068390328576
# 2068390211840
# 2068390211840  b and c have same object so same id
print(a is b) #false
print(c is b) #true
