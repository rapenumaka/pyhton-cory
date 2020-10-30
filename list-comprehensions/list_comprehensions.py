nums = [1,2,3,4,5,6,7,8,9,10]

my_list=[]

for n in nums:
    if(n%2==0):
        my_list.append(n)
        print(n)

 ### List comprehensions

 ## I want 'n' for each 'n' in nums

my_n_list = [n for n in nums]

print(my_n_list)

my_for_list = []

for n in nums:
    my_for_list.append(n)
print(my_for_list)

## Now using the list comprehension.. a list of squares from nums list

n_sqrs = [n**2 for n in nums]
print(n_sqrs)

## Use the list comprehensions.. create a list if n%3==0

div_by_3 = [n for n in nums if n%3==0]
print(div_by_3)


a = ['a', 'b', 'c','d']
n = [1,2,3,4]
## Generating a tuples
my_list = [ (l,m) for l in a for m in n ]

print(my_list)

### Creating zip  (a,1) (b,2), (c,3) (d,4)

p = ['a','b','c','d']
o = [1,2,3,4]

m = zip(p,o)

