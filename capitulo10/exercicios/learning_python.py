#!/usr/bin/python3

file = 'learning_python.txt'

# Print the entire file
with open(file) as file_object:
    learned = file_object.read()
    print(learned.rstrip())


# Print the entire file
with open(file) as file_object:
    for line in file_object:
        print(line.rstrip())

# Print a list
with open(file) as file_object:
    list = file_object.readlines()
print(list)
for line in list:
    print(line.rstrip())
