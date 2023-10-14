def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i 
    return -1  

numbers = [int(x) for x in input("Enter a list of numbers separated by space: ").split()]

target_number = int(input("Enter the number to search for: "))

result = linear_search(numbers, target_number)

if result != -1:
    print(f"The target number {target_number} is found at index {result}.")
else:
    print(f"The target number {target_number} is not found in the list.")
