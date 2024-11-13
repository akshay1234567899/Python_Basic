num = 19

if (num <= 1):
    print(f"The {num}  is NOT Prime Number")
else:
    prime = True  # suppose the no is prime no

    for i in range(1, int(num * 0.5) + 1):
        if (num % i == 0):
            prime = False
        else:
            prime = True

    if prime:
        print(f"The {num} is Prime Number")
    else:
        print(f"The {num}  is NOT Prime Number")