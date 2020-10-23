#!/usr/bin/python3

file = 'guest_book.txt'


def write_on_file(guest):
    """Function to write in file the name of guest."""
    with open(file, 'a') as file_object:
        file_object.write(guest.title() + "\n")

if __name__ == '__main__':
    print("To exit write 'exit'")
    while True:
        guest = input("Please, enter your name: ")
        if guest == 'exit':
            break
        write_on_file(guest)
