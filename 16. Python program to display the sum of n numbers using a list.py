n = int(input("Enter the number of elements: "))

numbers = [float(input(f"Enter number {i + 1}: ")) for i in range(n)]

total_sum = sum(numbers)

print(f"The sum of the numbers is: {total_sum}")