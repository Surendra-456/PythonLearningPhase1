

# =================================================
# 1. VARIABLES
# =================================================

name = "Surendra"
age = 25
height = 5.9
is_engineer = True

print(name, age, height, is_engineer)

# Check type
print(type(name))
print(type(age))

# =================================================
# 2. DATA TYPES
# =================================================

# String
text = "Hello"

# Integer
num = 10

# Float
price = 99.99

# Boolean
active = True

# List (Mutable)
colors = ["red", "green", "blue"]

# Tuple (Immutable)
coordinates = (10, 20)

# Set (Unique values)
nums = {1, 2, 3}

# Dictionary (Key-Value)
person = {
    "name": "John",
    "age": 30
}

# =================================================
# 3. FALSY VALUES
# =================================================

# All evaluate to False

False
None
0
0.0
''
""
[]
()
{}
set()

# Example
value = {}

if value:
    print("True")
else:
    print("False")

# =================================================
# 4. STRINGS
# =================================================

name = "Python"

print(name.upper())
print(name.lower())
print(name.title())
print(name.replace("Py", "My"))

# f-string
age = 30
print(f"My age is {age}")

# Slicing
print(name[0])
print(name[-1])
print(name[0:3])

# =================================================
# 5. LISTS
# =================================================

fruits = ["apple", "banana", "mango"]

fruits.append("orange")
fruits.insert(1, "kiwi")
fruits.remove("banana")

print(fruits)

for fruit in fruits:
    print(fruit)

# List comprehension
squares = [x*x for x in range(5)]
print(squares)

# =================================================
# 6. TUPLES
# =================================================

point = (10, 20)

x, y = point

print(x, y)

# =================================================
# 7. SETS
# =================================================

a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)  # union
print(a & b)  # intersection
print(a - b)  # difference

# =================================================
# 8. DICTIONARIES
# =================================================

user = {
    "name": "Surendra",
    "role": "Engineer"
}

print(user["name"])
print(user.get("age"))

for key, value in user.items():
    print(key, value)

# =================================================
# 9. CONDITIONS
# =================================================

age = 18

if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teen")
else:
    print("Child")

# Ternary
status = "Adult" if age >= 18 else "Minor"

# =================================================
# 10. LOOPS
# =================================================

# For loop
for i in range(5):
    print(i)

# While loop
count = 0

while count < 3:
    print(count)
    count += 1

# break
# continue
# pass

# =================================================
# 11. FUNCTIONS
# =================================================

def greet(name):
    return f"Hello {name}"

print(greet("Surendra"))


def add(a, b=0):
    return a + b

print(add(5, 3))

# Lambda
square = lambda x: x*x
print(square(4))

# =================================================
# 12. EXCEPTIONS
# =================================================

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("Done")

# =================================================
# 13. FILE HANDLING
# =================================================

with open("sample.txt", "w") as file:
    file.write("Hello World")

with open("sample.txt", "r") as file:
    content = file.read()

print(content)

# =================================================
# 14. CLASSES & OOP
# =================================================

class Person:

    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"Hi, I'm {self.name}")

p = Person("Surendra")
p.speak()

# Inheritance

class Employee(Person):

    def __init__(self, name, role):
        super().__init__(name)
        self.role = role

e = Employee("Surendra", "Engineer")

# =================================================
# 15. MODULES
# =================================================

import math

print(math.sqrt(25))

from datetime import datetime

print(datetime.now())

# =================================================
# 16. ENUMERATE & ZIP
# =================================================

names = ["A", "B", "C"]

for index, value in enumerate(names):
    print(index, value)

a = [1, 2, 3]
b = ["one", "two", "three"]

for x, y in zip(a, b):
    print(x, y)

# =================================================
# 17. UNPACKING
# =================================================

numbers = [1, 2, 3]

a, b, c = numbers

print(a, b, c)

# =================================================
# 18. *ARGS AND **KWARGS
# =================================================

def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4))


def show_info(**kwargs):
    print(kwargs)

show_info(name="Surendra", role="Engineer")

# =================================================
# 19. COMPREHENSIONS
# =================================================

squares = [x*x for x in range(10)]

evens = [x for x in range(10) if x % 2 == 0]

mapping = {x: x*x for x in range(5)}

# =================================================
# 20. COMMON PYTHONIC TRICKS
# =================================================

# Swap variables
a, b = b, a

# Membership
if "apple" in fruits:
    print("Found")

# Any / All
nums = [True, True, False]

print(any(nums))
print(all(nums))

# =================================================
# 21. USEFUL BUILT-IN FUNCTIONS
# =================================================

len([1, 2, 3])

max([1, 2, 3])

min([1, 2, 3])

sum([1, 2, 3])

sorted([3, 1, 2])

round(10.567, 2)

# =================================================
# 22. IMPORTANT DSA METHODS
# =================================================

stack = []

stack.append(10)
stack.pop()

from collections import deque

queue = deque()

queue.append(1)
queue.popleft()

# =================================================
# 23. VIRTUAL ENVIRONMENT
# =================================================

# Create
# python -m venv venv

# Activate Windows
# venv\\Scripts\\activate

# Activate Linux/Mac
# source venv/bin/activate

# =================================================
# 24. PIP
# =================================================

# pip install requests
# pip install pandas
# pip freeze
# pip list

# =================================================
# 25. MOST ASKED INTERVIEW TOPICS
# =================================================

"""
Mutable vs Immutable
List vs Tuple
Set vs Dict
Deep Copy vs Shallow Copy
*args vs **kwargs
is vs ==
Generator vs List
Multithreading vs Multiprocessing
Decorators
Context Managers
OOP Principles
Exception Handling
Time Complexity
"""

# =================================================
# END
# =================================================