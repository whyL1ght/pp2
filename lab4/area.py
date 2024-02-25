import math
def area_trapezoid(a, b, h):
    area = (a+b)/2 * h
    return area

a = float(input())
b = float(input())
h = float(input())
print(area_trapezoid(a,b,h))