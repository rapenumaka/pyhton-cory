




"""
why __name__ == '__main__'
When python runa files , it sends a few special variables
and "name" is one of them

When we import the module it


"""
print (__name__)  ## this gives __main__
print ("First Module's Name : {}".format(__name__))  ## this gives __main__


if __name__=='__main__':
    print ("Run Directly")
else:
    print(" running from import")