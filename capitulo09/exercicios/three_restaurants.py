#!/usr/bin/python3


class Restaurant:
    """Uma tentativa simples de modelar um restaurante."""

    def __init__(self, restaurant_name, cuisine_type):
        """Inicializa o nome e o tipo de comida."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Exibe o nome e a comida do restaurante."""
        print(f"O {self.restaurant_name} serve comida {self.cuisine_type}.")

    def open_restaurant(self):
        """Abre o restaurante."""
        print(f"O {self.restaurant_name} está aberto!")

restaurante_0 = Restaurant('Domingos', 'Italiana')
restaurante_1 = Restaurant('Nakoruru', 'Japonesa')
restaurante_2 = Restaurant('Batista', 'Bahiana')

restaurante_0.describe_restaurant()
restaurante_1.describe_restaurant()
restaurante_2.describe_restaurant()
