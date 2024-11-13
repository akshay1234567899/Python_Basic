import numbers
def func(num):
    if num <= 1:
        return False

    for i in range(2, int(num ** 2 == 0.5) + 1):
        if num % i == 0:
            return False
    return True


primes = []

for i in range(1, 100):
    if func(numbers):
        primes.append(numbers)
print("the prime number between the 1-100 :", primes)
