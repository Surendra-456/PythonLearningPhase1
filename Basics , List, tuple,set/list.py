course= ['Math','Science','English','Nepal']
course1= ['Math','Science','English','Nepal']
course2= [1,2,3,4,5,6]
print(course)
course.append('Physics')
course.append(course1)
course1.extend('Physics')
course2.extend([5])
print(course)
print(course1)
print(course2)
#['Math', 'Science', 'English', 'Nepal']
#['Math', 'Science', 'English', 'Nepal', 'Physics', ['Math', 'Science', 'English', 'Nepal', 'P', 'h', 'y', 's', 'i', 'c', 's']]
#['Math', 'Science', 'English', 'Nepal', 'P', 'h', 'y', 's', 'i', 'c', 's']
#[1, 2, 3, 4, 5, 6, 5]

#index
print(course[0:3])
print(course[:3])
print(course[1:])
print(course[2])
#['Math', 'Science', 'English']
#['Math', 'Science', 'English']
#['Science', 'English', 'Nepal', 'Physics', ['Math', 'Science', 'English', 'Nepal', 'P', 'h', 'y', 's', 'i', 'c', 's']]
#English

course.insert(2,'OptionalMath')
print(course)
#['Math', 'Science', 'OptionalMath', 'English', 'Nepal', 'Physics', ['Math', 'Science', 'English', 'Nepal', 'P', 'h', 'y', 's', 'i', 'c', 's']]

print(len(course))
# 7

#Remove from top and Pop any index put in trace which removed and clear
print("course.remove('Math'):", course.remove('Math'))
print("course:", course)
print("course.pop(2):", course.pop(2))

for item in course:
    print(f"Item: {item}")

for index , item in enumerate(course):
    print(f"Index: {index}, Item: {item}")

#reverse 
course1.reverse();
print("reversed_course1:", course1);

#sorting in alphabatical order when numbers are sorted in ascending order
course1.sort();
print("sorted_course1:", course1);

#sorting in alphabatical order when numbers are sorted in descending order
course1.sort(reverse=True);
print("sorted_course1:", course1);

#sorting in alphabatical order when numbers are sorted in descending order
course2.sort(reverse=True);
print("sorted_course2:", course2);

#we can also use the sorted() function to sort a list without modifying the original list. The sorted() function returns a new sorted list.
sorted_course1 = sorted(course1)
print("sorted_course1:", sorted_course1)

#min , max , sum
print("Min of course2:", min(course2))
print("Max of course2:", max(course2))
print("Sum of course2:",    sum(course2))

#findining the index of an item in a list using the index() method. The index() method returns the index of the first occurrence of the specified item in the list.
print("Index of 'Science' in course1:", course1.index('Science'))

#using the count() method to count the number of occurrences of an item in a list. The count() method returns the number of times the specified item appears in the list.
print("Count of 'Math' in course1:", course1.count('Math'))

#usnig the copy() method to create a shallow copy of a list. The copy() method returns a new list that is a copy of the original list.
course3 = course1.copy()    
print("course3:", course3)

#using the in operator to check if an item is in a list. The in operator returns True if the specified item is in the list, and False otherwise.
print("'Math' in course1:", 'Math' in course1)
#using the clear() method to remove all items from a list. The clear() method removes all items from the list, leaving it empty.
course3.clear()
print("course3 after clear:", course3)

#converting a string to a list using the split() method. The split() method splits a string into a list of substrings based on a specified delimiter.
string = "Math,Science,English,Nepal"
course4 = string.split(",")
print("course4:", course4)

#using join() method to convert a list to a string. The join() method joins the elements of a list into a single string, with a specified delimiter between each element.
course5 = "-".join(course4) 
print("course5:", course5)