def find_odd_numbers(arr):
    odd_numbers = [num for num in arr if num % 2 != 0]
    return odd_numbers

numbers = [int(x) for x in input("Enter an array of numbers separated by space: ").split()]

odd_numbers = find_odd_numbers(numbers)

print(f"The odd numbers in the array are: {odd_numbers}")
