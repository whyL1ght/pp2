import math
def squares(a, b):
    for i in range(a, b + 1):
        yield pow(i, 2)

a = int(input())
b = int(input())

for square in squares(a, b):
    print(square)