#!/usr/bin/python3

filename = 'pi_digits.txt'

with open(filename) as file_object:
    #v1.0 contents = file_object.read()
    #v1.2 for line in file_object:
    lines = file_object.readlines()
        #print(line)
        #v1.2 print(line.rstrip())
#v1.0 print(contents)
#v1.1 print(contents.rstrip())

for line in lines:
    print(line.rstrip())

print(lines)
