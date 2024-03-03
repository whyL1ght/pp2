import re
t = input()
x = re.findall(r"[A-Z][a-z]+",t)
print(x)