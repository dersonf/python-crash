#!/usr/bin/python3

from musers import Admin

user_admin = Admin('Carlos', 'Alberto', 28, 'Cuiabá', 'M')
user_admin.describe_user()
user_admin.privilegios.show_privileges()
