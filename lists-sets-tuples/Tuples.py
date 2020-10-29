"""
A Tuple is a collection of Python objects separated by commas.
In someways a tuple is similar to a list in terms of indexing,
nested objects and repetition but a tuple is immutable unlike lists which are mutable.

"""


tuple1 = (0 ,1, 2, 3)
print(tuple1[1:])
print(tuple1[::-1])
print(tuple1[2:4])

print(tuple1)

## Tupes are immutables, that mean we cant insert element

tuple1 = (0, 1, 2, 3)
try:
    tuple1[0] = 4
except TypeError:
    print('Python tuples are immutable')
print(tuple1)