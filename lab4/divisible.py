def divisible_by_3_and_4_generator(N):
    for i in range(N + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input())
divisible_nums = divisible_by_3_and_4_generator(n)

for num in divisible_nums:
    print(num)