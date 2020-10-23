#!/usr/bin/python3

file = 'programming_poll.txt'


def store_reason(reason):
    """Store the vote reason in file."""
    with open(file, 'a') as file_object:
        file_object.write(reason + "\n")


if __name__ == '__main__':
    print("To exit poll type 'exit':")
    while True:
        reason = input("Why you like programming? ")
        if reason == 'exit':
            break
        store_reason(reason)
