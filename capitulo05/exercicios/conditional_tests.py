#!/usr/bin/python3

car = 'subaru'
pizza = 'portuguesa'
carros = 'nao'
idade = 40
docker = 'sim'
kubernetes = 'sim'
python = 'nao'
ansible = 'sim'
filhos = ['gabriel', 'luiza']
esposa = 'patricia'
luiza = 15
gabriel = 4

print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

print("\nSua pizza favorita é portuguesa? Eu acho que sim.")
print(pizza == 'portuguesa')

print("\nSua pizza favorita é calabreza: Eu acho que não.")
print(pizza == 'calabreza')

print("\nVocê gosta de carros?")
print(carros == 'sim')

print("\nVocê é maior de idade?")
print(idade >= 18)

print("\nVocê já pode ter carteirinha pra não pagar passagem?")
print(idade >= 65)

print("\nVocê domina python?")
print(python == 'sim')

print("\nVocê domina docker?")
print(docker == 'sim')

print("\nVocê domina kubernetes?")
print(kubernetes == 'sim')

print("\nVocê domina ansible?")
print(ansible == 'sim')

print("\nVocê tem uma filha chamada Luiza?")
print('Luiza'.lower() in filhos)

print("\nVocê tem dois filhos?")
print(len(filhos) == 2)

print("\nVocê tem um filhos chamado patricia?")
print('patricia' in filhos)

print("\nO nome da pizza é portuguesa?")
print(pizza == 'portuguesa')

print("\nO nome da pizza não é portugueza com z?")
print(pizza != 'portugueza')

print("\nO nome da esposa é PaTrIciA?")
print('PaTrIciA'.lower() == esposa)

print("\nSeus dois filhos são menores de idade?")
print(luiza <= 18 and gabriel <= 18)

print("\nGabriel tem 4 anos?")
print(gabriel == 4)

print("\nLuiza não tem 4 anos?")
print(luiza != 4)

print("\nLuiza é maior de 18 anos?")
print(luiza > 18)

print("\nLuiza tem idade igual ou superior a 15 anos?")
print(luiza >= 15)
