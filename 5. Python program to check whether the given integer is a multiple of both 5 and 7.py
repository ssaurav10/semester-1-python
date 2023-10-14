def is_multiple_of_5_and_7(number):
    return number % 5 == 0 and number % 7 == 0

integer = int(input("Enter an integer: "))

if is_multiple_of_5_and_7(integer):
    print(f"{integer} is a multiple of both 5 and 7.")
else:
    print(f"{integer} is not a multiple of both 5 and 7.")