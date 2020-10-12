#!/usr/bin/python3


def city_country(city, country):
    """Retorna o nome da cidade e do pais"""
    return f"{city.title()}, {country.title()}"


print(city_country('são paulo', 'brasil'))
print(city_country('santiago', 'chile'))
print(city_country('bogotá', 'colômbia'))
print(city_country('sydney', 'austrália'))
