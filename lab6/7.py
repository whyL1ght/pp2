import os
import string
def my_func(f):
    with open(f, "r") as file:
        bll=file.read()

    newf="newf.txt"

    with open(newf, "w") as file:
        file.write(bll)

a = "C:\pp2\lab6\pp2.txt"
my_func(a)