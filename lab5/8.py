import re
t = input()
x = re.findall(r"[^A-Z]*[A-Z][^A-Z]*",t)
result = ' '.join(x)
print(result)