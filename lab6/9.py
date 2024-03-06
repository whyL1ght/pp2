import time
import math

nums = input().split()
some_list = [int(num) for num in nums]
def pr(l):
    p = 1
    for i in l:
        p = eval("p*i")
    return p
print("product:", pr(some_list))