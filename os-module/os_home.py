import os

## to get the present working directory
print(os.getcwd())

## To navigate to the path /Users/arvind.penumaka/Documents/roar/

os.chdir('/Users/arvind.penumaka/Documents/roar/')

print(os.getcwd())


## To access the home directory  IN LINUX its similar to $echo $HOME
print(os.environ.get('HOME'))

### os.path.join

file_path = os.path.join(os.environ.get('HOME'),'test.txt')

print(file_path)

## os.path.basename ---- grabs the base name , this doesn't need to be file that exist

print(os.path.basename('my/nonsense/file.txt')) ## This gives files.txt

print(os.path.split('my/nonsense/file.txt'))

## To check if the path exist

print(os.path.exists('my/nonsense/file.txt'))  ## This gives False

## To check if the path a directory

print(os.path.isdir('/Users/arvind.penumaka/Documents/roar/'))  ## this give True

print(os.path.islink('/Users/arvind.penumaka/Documents/roar/renamed.txt'))  ## This renamed.txt exist, so this gives True

## This is a useful method to split the extension of the file and pathpf file
print(os.path.splitext('/tmp/test.pdf'))

