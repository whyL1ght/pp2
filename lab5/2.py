import re
t = input()
x = re.search(r"ab{2,3}", t)
print(x)