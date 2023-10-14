def fibonacci_recursive(n):
    if n <= 0:
        return "Invalid input, please enter a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

N = int(input("Enter the value of N: "))

result = fibonacci_recursive(N)
print(f"The {N}th term in the Fibonacci series is: {result}")
