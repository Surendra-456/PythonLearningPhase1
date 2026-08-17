from operator import attrgetter
li = [9,1,8,2,7,3,6,4,5]
#sorted() Returns a new sorted list. Does not modify the original list.
s_li = sorted(li, reverse=True)

print('Sorted Variable:\t', s_li)
#Sorts the list in place. Modifies the original list. Returns None.
li.sort(reverse=True)

print('Original Variable:\t', li)

tup = (9,1,8,2,7,3,6,4,5)
s_tup = sorted(tup)
print('Tuple\t', s_tup)

di = {
    'name': 'Corey',
    'job': 'programming',
    'age': None,
    'os': 'Mac'
}
#When sorted() is used on a dictionary, it sorts the dictionary keys by default.
s_di = sorted(di)
print('Dict\t', s_di)


li = [-6, -5, -4, 1, 2, 3]
#Sorts the list based on the absolute values of its elements.
s_li = sorted(li, key=abs)

print(s_li)

# ==========================================
# Employee Sorting Example
# ==========================================

# Create a class named Employee.
# A class is a blueprint for creating objects.

class Employee():
    # Constructor
    # Runs automatically when an Employee object is created.
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    # Controls how the object is displayed when printed.
    def __repr__(self):
        return '({}, {}, ${})'.format(
            self.name,
            self.age,
            self.salary
        )


# Create Employee objects
e1 = Employee('Carl', 37, 70000)
e2 = Employee('Sarah', 29, 80000)
e3 = Employee('John', 43, 90000)

# Store all employees in a list
employees = [e1, e2, e3]

# ------------------------------------------
# Sorting Function
# ------------------------------------------

# This function receives one employee object.
# It returns the employee's name.
# The returned value will be used for sorting.

def e_sort(emp):
    return emp.name

# Sort employees using their names.
# Python calls e_sort() for every employee.
#
# e_sort(e1) -> "Carl"
# e_sort(e2) -> "Sarah"
# e_sort(e3) -> "John"
#
# Python then sorts alphabetically:
# Carl, John, Sarah

#s_employees = sorted(employees, key=e_sort)
s_employees = sorted(employees, key=attrgetter('age'))
#s_employees = sorted(employees, key=lambda emp: emp.salary,reverse=True)


# Print sorted employees
print(s_employees)

# Output:
# [(Carl, 37, $70000),
#  (John, 43, $90000),
#  (Sarah, 29, $80000)]

# s_employees = sorted(employees, key=lambda e: e.salary)

# print(s_employees)
