def is_prime(n):
    if n <= 1: return False
    if n == 2: return True
    if n % 2 == 0: return False
    i = 3
    while i * i <= n:
        if n % i == 0: return False
        i += 2
    return True

def find_primes(start, end):
    return [num for num in range(start, end) if is_prime(num)]

def calculate_power_sum(n):
    return sum(n**i for i in range(1, 101))
