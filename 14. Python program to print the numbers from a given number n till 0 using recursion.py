def print_numbers_reverse(n):
    if n >= 0:
        print(n, end=' ')
        print_numbers_reverse(n - 1)

n = int(input("Enter a number: "))

print_numbers_reverse(n)