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
        self.login_attempts = 0
        self.admin = 0
        self.privilegios = Privileges(self.admin)

    def describe_user(self):
        """Exibe as informações do usuário."""
        print(f"\nnome: {self.first_name}\n"
              f"último nome: {self.last_name}\n"
              f"idade: {self.age}\n"
              f"cidade: {self.city}\n"
              f"tentativas de login: {self.login_attempts}")
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

    def increment_login_attempts(self):
        """Incrementa em +1 a quantidade de tentativa de login."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reinicia a quantidade de tentativas de login."""
        self.login_attempts = 0

    def get_admin(self):
        """Informa se é admin ou não."""
        if self.admin == 0:
            print(f"Usuário {self.first_name} comum.")
        if self.admin == 1:
            print(f"Usuário {self.first_name} Admin.")


class Privileges:
    """Representa os privilegios de um usuario."""

    def __init__(self, admin):
        """Inicializa o atributo privilégios."""
        if admin == 0:
            self.privilegios = "POST em seu Blog"
        if admin == 1:
            self.privilegios = (
                "POST em qualquer Blog, criar usuários, "
                "banir usuários."
            )

    def show_privileges(self):
        """Exibe os privilégios do usuário."""
        print(f"Possui privilégios: {self.privilegios}")


class Admin(User):
    """Cria um usuário administrador."""

    def __init__(self, first_name, last_name, age, city, sexo):
        """Inicializa usuário administrador."""
        super(). __init__(first_name, last_name, age, city, sexo)
        self.admin = 1
        self.privilegios = Privileges(self.admin)


user_0 = User('Jonathas', 'Guimarães', 28, 'São Paulo', 'M')
user_0.describe_user()
user_0.get_admin()
user_0.privilegios.show_privileges()

admin_0 = Admin('Jânia', 'Quadros', 72, 'Paraíba', 'M')
admin_0.describe_user()
admin_0.get_admin()
admin_0.privilegios.show_privileges()
