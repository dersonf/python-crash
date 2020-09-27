#!/usr/bin/python3

current_users = ['anderson', 'patricia', 'luiza', 'gabriel', 'neuza']
new_users = ['anderson', 'patricia', 'nivaldo', 'amanda', 'maria']

for new_user in new_users:
    if new_user.lower() in current_users:
        print(f"Usuário {new_user} já em uso, utilize outro!")
    else:
        print(f"Usuário {new_user} disponível.")
