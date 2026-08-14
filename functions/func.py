def first():
    return 1  #explicit return
def second():
    print(2)  #implicit 

print(first())
print(second())
second()

#function with parameters
def employeeName(greeting, name):
    #return '{} {}'.format(greeting, name)  #using format method
    #the purpose of f is to embed variables and expressions directly into strings in a readable way.
    return f"{greeting}, {name}!"

print(employeeName("Hello", "Alice"))


# *args takes any number of positional arguments and returns them as a tuple. and **kwargs takes any number of keyword arguments and returns them as a dictionary.
def studentInfo(*args, **keyvalue):
    print("args:", args)
    print("keyvalue:", keyvalue)

studentInfo("Ram",20,name="Shuya,",city="Kathmandu")
# args: ('Ram', 20)
# keyvalue: {'name': 'Shuya,', 'city': 'Kathmandu'}



# Number of days per month. First value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    #"""Return True for leap years, False for non-leap years."""

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    #"""Return number of days in that month in that year."""

    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]

print(is_leap(2020))
print(days_in_month(2020,3))