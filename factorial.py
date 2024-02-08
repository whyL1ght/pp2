def calculate_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n-1)

n = int(input())
print(calculate_factorial(n))