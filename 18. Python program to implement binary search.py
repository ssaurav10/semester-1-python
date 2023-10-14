def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_value = arr[mid]

        if mid_value == target:
            return mid 
        elif mid_value < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1 

numbers = [int(x) for x in input("Enter a sorted list of numbers separated by space: ").split()]

target_number = int(input("Enter the number to search for: "))

result = binary_search(numbers, target_number)

if result != -1:
    print(f"The target number {target_number} is found at index {result}.")
else:
    print(f"The target number {target_number} is not found in the list.")