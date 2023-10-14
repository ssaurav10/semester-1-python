def generate_primes_in_range(n):
    primes = []
    for num in range(2, n+1):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

N = int(input("Enter the upper limit (N): "))

result = generate_primes_in_range(N)
print(f"Prime numbers in the range from 1 to {N}: {result}")