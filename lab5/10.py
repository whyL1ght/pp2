import re
t = input()
x = re.sub(r"(?<!^)(?=[A-Z])","_",t).lower()
print(x)