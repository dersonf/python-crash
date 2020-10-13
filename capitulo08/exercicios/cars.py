#!/usr/bin/python3


def make_car(manufacturer, model, **characteristics):
    characteristics['manufacturer'] = manufacturer
    characteristics['model'] = model
    return characteristics


car = make_car('subaru', 'outback',
               color='blue',
               tow_package=True)
print(car)
car = make_car('chevrolet', 'corsa',
               color='prata',
               motor='mpfi',
               combustivel='gasolina')
print(car)
car = make_car('volkswagem', 'gol',
               color='vermelho',
               combustivel='flex',
               ano=2019)
print(car)
