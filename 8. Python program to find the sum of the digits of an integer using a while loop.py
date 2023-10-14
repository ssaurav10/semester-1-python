def sum_of_digits(n):
    digit_sum = 0

    while n > 0:
        digit = n % 10

        digit_sum += digit

        n = n // 10

    return digit_sum

integer = int(input("Enter an integer: "))

result = sum_of_digits(integer)

print(f"The sum of the digits of {integer} is: {result}")