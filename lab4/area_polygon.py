import math
def area_of_polygon(a, b):
    area = (a * pow(b,2)) / (4 * math.tan(math.pi/ a))
    return area

a = int(input())
b = float(input())
print(area_of_polygon(a, b))