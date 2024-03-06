import os
def to_list(f):
    listtof=[1, 2, 3]

    with open(f, "a") as file:
        file.write(", ".join(str(i) for i in listtof))


def to_file(f):
    with open(f, "r") as file:
        print(file.read())


filename="C:\pp2\lab6\pp2.txt"

to_list(filename)
to_file(filename)