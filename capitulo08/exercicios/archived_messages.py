#!/usr/bin/python3

messages = [
    'O pato faz qua.',
    'O Gabriel enrola pra comer.',
    'O telhado tem vazamentos.',
    'Meu celular quebrou.',
]
sent_messages = []


def send_messages(messages):
    while messages:
        message = messages.pop()
        print(message)
        sent_messages.append(message)


send_messages(messages[:])
print(f"\nMensagens para enviar:\n{messages}"
      f"\nMensagens enviadas.\n{sent_messages}")
