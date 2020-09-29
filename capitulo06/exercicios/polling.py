#!/usr/bin/python3

linguagem_favorita = {
    'jilo': 'python',
    'rogerio': 'java',
    'anderson': 'bash',
    'grazi': 'python',
    'maria cristina': 'c#',
    'joao': 'java',
    }
convite = [
    'jilo',
    'rogerio',
    'daiane',
    'thais',
    'anderson',
    'maria cristina',
    'miguel',
    'joao',
    'renato',
    ]

for nome in convite:
    if nome in linguagem_favorita:
        print(f"{nome.title()} obrigado por responder a pesquisa!")
    else:
        print(f"{nome.title()} poderia responde a pesquisa por favor?")
