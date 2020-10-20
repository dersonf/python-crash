#!/usr/bin/python3

from madmin import Admin, Privileges

#user_admin = Admin('Carlos', 'Alberto', 28, 'Cuiabá', 'M')
admin = Admin('Fernanda', 'Caldas', 32, 'Londrina', 'F')
admin.describe_user()
admin.privilegios.show_privileges()
