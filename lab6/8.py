import os
import string
my_file = "C:\pp2\lab6\8.txt"

def deletor(f):
    if not os.path.exists(f):
        print("Doesn't exist")
    else:
        if not os.access(f, os.X_OK):
            print("Not access")
        else:
            os.remove(f)
            print("Deleted")
deletor("my_file")