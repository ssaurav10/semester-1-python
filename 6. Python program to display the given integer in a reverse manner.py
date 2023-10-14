def reverse_integer_twice(number):
    reversed_str = str(number)[::-1]

    result = int(reversed_str[::-1])

    return result

integer = int(input("Enter an integer: "))

result = reverse_integer_twice(integer)
print(f"The integer {integer} in 2 reverse manner is: {result}")
