import re
t = input()
x = re.findall(r"[A-Z][^A-Z]*",t)
res = ' '.join(x)
print(res)