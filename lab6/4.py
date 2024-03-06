def count_l(f):
    with open(f, "r") as file:
        num=0
        for line in file:
            num+=1
    return num


filename="C:\pp2\lab6\pp2.txt"
print("num of lines:", count_l(filename))