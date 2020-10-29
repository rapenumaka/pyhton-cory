"""
Lists - sequential data

The important characteristics of Python lists are as follows:
   -Lists are ordered.
   -Lists can contain any arbitrary objects.
   -List elements can be accessed by index.

"""

course = ['maths', 'physics', 'chemisty', 'history','computer science']

print(course)

## Number of elements in list

print(len(course))

## To access the values of the lists using the indexes

print(course[0])
print(course[2])

## Since we dont have index 10
try:
    print(course[10])
except IndexError:
    print("Index does not exist")

## To get the last item .. we can use negetive index

print(course[-1])

## To get the last but second

print(course[-2])

## get the list of all the elements from index 0 to 2

print(course[0:3])  ## this will only give element at index 0,1,2

print(course[0:-1])  ## This will give everything EXCEPT the last element

print(course[2:])  ## GIves the list of elements from index 2 all the way to end

## Storing the list in the reverse order

reversed_courses = course[::-1]



print(reversed_courses)

## To append the element to the list

## To add it to the end

course.append('english')

print(course)

## We can also insert the element at a particular location

for s in course:
    print('{} is present at index -------- {}'.format(s,course.index(s)))

course.insert(2,'biology')
print('added the biology to index 2')

for s in course:
    print('{} is present at index -------- {}'.format(s,course.index(s)))

print()

## When we have multiple values to be added to the current list, we use extend methos

other_course = ['zoology', 'political science']

course.extend(other_course)

for s in course:
    print('{} is present at index -------- {}'.format(s,course.index(s)))



####  To remove the element from the list-- use remove if you what element you want to remove


print(course)
course.remove('maths')


print(course)

## Pop() methods remove the last element from the list and return the element that was removed
y =course.pop()

print('The following element was popped from the list :: {}'.format(y))

print(course)

## Sorting the list

course.sort()

print(" Using the sort method to print it alphabetically")

print(course)
print(" Using the sort method  and setting the reverse = True , to print it alphabetically in descending order ")

course.sort(reverse=True)

print(course)

nc = [1,2 ,3 ,'rabbit', 'apple', 'cat', 'zebra']

print(nc)
try:
    nc.sort()
except TypeError:
    print("Python will not sort the list that have both strings and integers")

print(nc)

## uSING THE course.sort() is altering the object course, to avoid this use the methed sorted(<object>)

course_sorted = sorted(course)
print(course)
print(course_sorted)


### Checkking if the element is present in the list use "IN"

print('biology' in course)  ## this gives True

print('anthropology' in course)  ## this gives True

## enumerate() gives both the index and element in the course

for index, element in enumerate(course):
    print("element {} is present at index {}".format(element, index))

## Converting the list to String , separting by -

print(course)

course_str = '-'.join(course)
course_star = '*'.join(course)
print(" Converted the list to a big String")
print(course_str)
print(course_star)

## Converting the String to list

course_list = course_str.split('-')

print(course_list)




z = []
try :
    print(z.pop())
except:
    print('there is no element to pop from the list')

