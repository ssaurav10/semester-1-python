def find_largest_number(arr):
    if not arr:
        return None  

    largest = arr[0]

    for num in arr:
        if num > largest:
            largest = num

    return largest

numbers = [int(x) for x in input("Enter a list of numbers separated by space: ").split()]

largest_number = find_largest_number(numbers)

if largest_number is not None:
    print(f"The largest number in the list is: {largest_number}")
else:
    print("The list is empty.")