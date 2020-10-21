#!/usr/bin/python3

from random import choice

series = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'A', 'B', 'C', 'D', 'E']
my_tickets = ['11AB', '35D6']


def sort_ticket():
    ticket = ''
    for count in range(1, 5):
        ticket += str(choice(series))
    return ticket

if __name__ == '__main__':
    count = 0
    while True:
        count += 1
        ticket_sorted = sort_ticket()
        if ticket_sorted in my_tickets:
            print("You win a prize!")
            print(f"A total of {count} times sorted "
                  f"with serie {ticket_sorted}.")
            break
