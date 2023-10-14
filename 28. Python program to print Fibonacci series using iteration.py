def fibonacci_iterative(n):
    fib_series = [0, 1]
    for i in range(2, n):
        fib_series.append(fib_series[i - 1] + fib_series[i - 2])
    return fib_series

num_terms = int(input("Enter the number of terms in the Fibonacci series: "))

result = fibonacci_iterative(num_terms)
print(f"The first {num_terms} terms in the Fibonacci series are: {result}")
