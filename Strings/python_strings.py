"""
Namespace is a way to implement scope. In Python, each package, module, class, function and method function owns a "namespace" in which variable names are resolved. When a function,  module or package is evaluated (that is, starts execution), a namespace is created. Think of it as an "evaluation context". When a function, etc., finishes execution, the namespace is dropped. The variables are dropped. Plus there's a global namespace that's used if the name isn't in the local namespace.

Each variable name is checked in the local namespace (the body of the function, the module, etc.), and then checked in the global namespace.

Variables are generally created only in a local namespace. The global and nonlocal statements can create variables in other than the local namespace.



"""
## Printing a message on console

print("Hello message")

## Create a string variable


### To reverse the String

name = "iphone"
print(name[::-1]) ## enohpi

message = " Hello, there "
print(message)

quotes = """Shop keeper said " it was Keren's order" """

print(quotes)

## TO ACCESS THE CHARACTER OF THE MESSAGE , using the index
## If you access the index that doesnt exist is

word = 'Hello World'

print(word[0])
print(word[2])
print("++++++++++++++++++++++++++++++++++++++++++")
for letter in word:
    print(letter)
    print()
print("++++++++++++++++++++++++++++++++++++++++++")

## The range of word

print(word[0:5])  ## Hello

print(word[6:11]) ## World

### Converter to lower

print(word.lower()) ## To lower
print(word.upper()) ## To upper
print(word.lower().count('hello')) ## 1
print(word.lower().count('l')) ## 1

## Replace the word ..

universe = "Hello Universe"

replace1 = universe.replace("Universe","GalAXY")

print(universe)
print(replace1)



######## Using the formated Strin

greet= 'Namaste'
my_name='Arvind'
my_message = '{}.{}. Welcome'.format(greet,my_name)
print(my_message)


##Using the f strings , only available in 3.6+
## Adding the variables directly using the placeholders

greeting = 'Hello'
name = 'Micheal'

message = f'{greeting},{name.upper()}. Welcome'
print(message)


#### TO see all the methods accessible to that variables

print(dir(message))

### To get the help  on string class

print(help(str))

### To get the help on string lower

print(help(str.lower))


