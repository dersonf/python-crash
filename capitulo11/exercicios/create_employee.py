#!/usr/bin/python3

from employee import Employee

employee_one = Employee('Adão', 'Sales', 2000)
print(employee_one.annual_salary)
employee_one.give_raise(200)
print(employee_one.annual_salary)
employee_one.give_raise()
print(employee_one.annual_salary)
