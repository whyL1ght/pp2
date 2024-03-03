import re
t = input()
x = re.findall(r".*a.*b$",t)
print(x)