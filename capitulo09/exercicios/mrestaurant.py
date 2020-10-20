"""Classes usadas para representar um restaurante."""


class Restaurant:
    """Uma tentativa simples de modelar um restaurante."""

    def __init__(self, restaurant_name, cuisine_type):
        """Inicializa o nome e o tipo de comida."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Exibe o nome e a comida do restaurante."""
        print(f"O {self.restaurant_name} serve comida {self.cuisine_type}")

    def open_restaurant(self):
        """Abre o restaurante."""
        print(f"O {self.restaurant_name} está aberto!")


class IceCreamStand(Restaurant):
    """Representa um stand de sorvetes em um restaurante."""

    def __init__(self, restaurant_name, cuisine_type):
        """
        Inicializa os atributos de uma classe filha.
        Inicializa os atributos dos sorvetes.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = [
            'chocolate',
            'morango',
            'baunilha',
            'creme',
            'coco',
            'limão',
        ]

    def get_flavors(self):
        """Print the available flavors of ice-cream."""
        print("We have the folowers flavors:")
        for flavor in self.flavors:
            print(f"\t- {flavor}")
