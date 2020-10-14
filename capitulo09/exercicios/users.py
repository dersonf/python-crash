#!/usr/bin/python3


class User:
    """Cria um simples usuário."""

    def __init__(self, first_name, last_name, age, city, sexo):
        """Inicializa nome do usuário."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.sexo = sexo

    def describe_user(self):
        """Exibe as informações do usuário."""
        print(f"\nnome: {self.first_name}\n"
              f"último nome: {self.last_name}\n"
              f"idade: {self.age}\n"
              f"cidade: {self.city}")
        if self.sexo == 'M':
            print("sexo: Masculino")
        if self.sexo == 'F':
            print("sexo: Feminino")
       
    def greet_user(self):
        """Exibe uma saudação ao usuário."""
        if self.sexo == 'M':
            print(f"Bem vindo de volta {self.first_name}!!!")
        elif self.sexo == 'F':
            print(f"Bem vinda de volta {self.first_name}!!!")


user_0 = User('Jonathas', 'Guimarães', 28, 'São Paulo', 'M')
user_1 = User('José', 'Fialho', 32, 'Maringá', 'M')
user_2 = User('Marina', 'Jesus', 22, 'Rio de Janeiro', 'F')
user_3 = User('Luciana', 'Ventura', 55, 'Bertioga', 'F')
user_4 = User('Márcio', 'Gonzales', 23, 'Goiânia', 'M')

user_0.describe_user()
user_1.describe_user()
user_2.describe_user()
user_3.describe_user()
user_4.describe_user()

user_0.greet_user()
user_1.greet_user()
user_2.greet_user()
user_3.greet_user()
user_4.greet_user()
