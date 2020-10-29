import os
from datetime import datetime

## To lean about all the methods in that os module

print(dir(os))

print('------------------------------------------------')
## To print the current workingdirectory

print(os.getcwd())

## To navigate to new location for example navigating to  :: /Users/arvind.penumaka/Documents/roar/
os.chdir('/Users/arvind.penumaka/Documents/roar/')

print(os.getcwd())

## To see all the files and folders present in the current directory

print(os.listdir())

## Creating a folder in the current working directory, lets create a folder
try:
    os.mkdir('os-demo')
except FileExistsError:
    print(" The folder already exists")

## To create a folder with multiple sub directories in the current working directory

try:
    os.makedirs('test-1/sub-1/sub-2/')
except FileExistsError:
    print(" The folders alredy exists")


## To delete the directory, lets delete the directory 'os-demo' that was created
try:
    os.rmdir('os-demo')
except FileNotFoundError:
    print(" The directory was not found")

## To delete the directory, lets delete the directory  with sub-directies'test-1' that was created


print(os.listdir())



## To to rename the file :: rename the test.txt to rename.txt
## mv file.ext new_name.ext
try:
    print(os.rename('test.txt','renamed.txt'))
except FileNotFoundError:
    print(" File test.txt does not exist")


print(os.listdir())

## Get all the information on renamed.txt

print(os.stat('renamed.txt'))

mod_time =os.stat('renamed.txt').st_mtime

print(datetime.fromtimestamp(mod_time))

### List of folders that were last modified

for m in os.listdir():
    print("{} was last modified on {}".format(m,datetime.fromtimestamp(os.stat(m).st_mtime)))


## os.walk returns tuples dirpath, dirnames, filename
## This is similar to tree
for dirpath, dirnames,filenames in os.walk('/Users/arvind.penumaka/Documents/roar/'):
    print("Current path :",dirpath)
    print("Files :",filenames)
    print("Directores: ",dirnames)
    print()











