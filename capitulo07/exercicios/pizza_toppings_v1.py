#!/usr/bin/python3

prompt = ("\nInforme as coberturas da pizza.")
prompt += ("\nDigite fim para encerrar: ")
message = ""
coberturas = []

while message != 'fim':
    message = input(prompt)
    if message != 'fim':
        coberturas.append(message)

print("Adicionamos as coberturas a sua pizza!")
for cobertura in coberturas:
    print(f"\r{cobertura.title()}")
