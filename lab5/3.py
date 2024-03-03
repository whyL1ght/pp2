import re
t = input()
x = re.findall(r"[a-z_]+_[a-z]+",t)
print(x)