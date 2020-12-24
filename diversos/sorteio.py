from random import sample
from sys import exit

sorteios = 0
bilhetes = [
    # 10 numeros
    # [2, 8, 14, 35, 12, 59, 13, 18, 27, 44],
    [2, 8, 14, 1, 16, 24, 13],
    [5, 7, 15, 13, 47, 36, 27],
    [23, 27, 42, 21, 38, 44, 43],
    [34, 48, 1, 60, 20, 45, 21],
    [6, 8, 12, 15, 25, 26, 18],
    [1, 2, 34, 38, 44, 18, 57],
    [23, 38, 37, 44, 52, 27, 6],
]


def sortear():
    """Sorteia numero da Mega Sena."""
    return sample(range(1, 61),k=6)


def confere(sorteado, bilhete):
    """Confere bilhete."""
    s = sorteado
    b = bilhete
    acertos = 0
    for n in b:
        if n in s:
            acertos += 1
            if acertos == 6:
                print(f"Voce acertou, foram {sorteios} sorteios.\nbilhete {bilhete}")
                exit()
   

while True:
    sorteado = sortear()
    sorteios += 1
    for bilhete in bilhetes:
        confere(sorteado, bilhete)

