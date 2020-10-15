#!/usr/bin/python3


class Restaurant:
    """Uma tentativa simples de modelar um restaurante."""

    def __init__(self, restaurant_name, cuisine_type):
        """Inicializa o nome e o tipo de comida."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Exibe o nome e a comida do restaurante."""
        print(f"O {self.restaurant_name} serve comida {self.cuisine_type}")

    def open_restaurant(self):
        """Abre o restaurante."""
        print(f"O {self.restaurant_name} está aberto!")

    def clientes_servidos(self):
        """Exibe quantos pratos foram servidos."""
        print(f"O {self.restaurant_name} serviu {self.number_served}.")

    def set_number_served(self, clientes):
        """Insere a quantidade de clientes atendidos."""
        self.number_served = clientes

    def increment_number_served(self, clientes):
        """Adiciona a quantidade de clientes atendidos."""
        self.number_served += clientes
        print("a day of business.")

restaurante = Restaurant('Domingos', 'Italiana')
restaurante.describe_restaurant()

restaurante.clientes_servidos()
#print(f"O {restaurante.restaurant_name} serviu {restaurante.number_served}")
#restaurante.number_served = 36
restaurante.set_number_served(36)
restaurante.clientes_servidos()
restaurante.increment_number_served(12)
restaurante.clientes_servidos()

#print(f"O nome do restaurante é {restaurante.restaurant_name}.")
#print(f"O tipo de comida é {restaurante.cuisine_type}.")
