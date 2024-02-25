import math
def degrees_to_radian(degrees):
    radians = degrees * (math.pi/180)
    return radians

degress = float(input())
print(degrees_to_radian(degress))
