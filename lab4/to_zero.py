def n_to_zero(n):
    for i in range(n, -1, -1):
        yield i

n = int(input())
nums = n_to_zero(n)

for num in nums:
    print(num)