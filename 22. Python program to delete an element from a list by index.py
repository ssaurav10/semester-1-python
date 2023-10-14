def delete_element_by_index(lst, index):
    if index < 0 or index >= len(lst):
        print("Invalid index.")
        return

    deleted_element = lst.pop(index)
    print(f"Element {deleted_element} at index {index} has been deleted.")

numbers = [int(x) for x in input("Enter a list of numbers separated by space: ").split()]

delete_index = int(input("Enter the index to delete: "))

delete_element_by_index(numbers, delete_index)

print("Updated list:", numbers)