def insert_number_at_position(lst, number, position):
    if position < 0 or position > len(lst):
        print("Invalid position.")
        return

    lst.insert(position, number)
    print(f"{number} has been inserted at position {position}.")

numbers = [int(x) for x in input("Enter a list of numbers separated by space: ").split()]

inserted_number = int(input("Enter the number to insert: "))

insert_position = int(input("Enter the position to insert the number: "))

insert_number_at_position(numbers, inserted_number, insert_position)

print("Updated list:", numbers)