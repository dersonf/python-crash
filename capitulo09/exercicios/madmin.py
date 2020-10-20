"""Modulo que contém classes para criação de adminitradores."""
from muser import User


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
