#!/usr/bin/python3

from random import choice

series = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'A', 'B', 'C', 'D', 'E']


def sort_ticket():
    ticket = ''
    for count in range(1, 5):
        ticket += str(choice(series))
    print(f"The ticket serie '{ticket}' win a prize!!!")

if __name__ == '__main__':
    sort_ticket()
