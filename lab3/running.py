def calculate_running_average(n):
    sum = 0
    running_average = []
    for i in range(1, len(n) + 1):
        sum += n[i - 1]
        running_average.append(sum/i)
    return running_average

n = input().split()
print(calculate_running_average(n))