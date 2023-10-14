def calculate_product(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

numbers_str = input("Enter a set of real numbers separated by spaces: ")

numbers = [float(x) for x in numbers_str.split()]

if numbers:
    product = calculate_product(numbers)
    print(f"The product of the numbers {numbers} is: {product}")
else:
    print("Please enter a valid set of real numbers.")