
def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

for number in range(100, 201):
    digit_sum = sum_of_digits(number)
    if digit_sum % 2 == 0:
        print(number)