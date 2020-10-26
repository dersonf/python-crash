#!/usr/bin/python3


def read_file(filename):
    """Read a file."""
    try:
        with open(filename) as f:
            content = f.read()
    except FileNotFoundError:
        print(f"{filename} not found.")
    else:
        print(content)

files = ['cats.txt', 'dogs.txt']
for file in files:
    read_file(file)
