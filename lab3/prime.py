def is_prime(n):
    if n < 2:
        return False
    for i in range (2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(a):
    primes = [num for num in a if is_prime(num)] 
    return primes

numbers = input().split()
numbers = [int(num) for num in numbers]
primes = filter_prime(numbers)
print(primes)