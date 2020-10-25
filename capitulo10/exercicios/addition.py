#!/usr/bin/python3

while True:
    print("\nEnter 'q' to exit.")
    first_number = input("Insert a number: ")
    if first_number == 'q':
        break
    second_number = input("Insert another number: ")
    if second_number == 'q':
        break

    try:
        numbers_sum = int(first_number) + int(second_number)
    except ValueError:
        print("Insert a number not a letter.")
    else:
        print (f"The sum is equal {numbers_sum}")
