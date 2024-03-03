import re
t = input()
x = re.sub(r"[., ]",":",t)
print(x)