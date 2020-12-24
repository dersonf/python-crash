from random import sample
from sys import exit


class NumerosSorteados:
    """Sorteia numeros da loteria."""

    def __init__(self, inicio=1, fim=60, qtdd=6):
        """Inicializa classe de sorteio"""
        self.inicio = inicio
        self.fim = fim + 1
        self.qtdd_numeros = qtdd
        self.sorteios = 0

    def sortear(self):
        """Sorteia numeros."""
        self.sorteado = sample(
            range(self.inicio, self.fim), k=self.qtdd_numeros
        )
        self.sorteios += 1

    def conferir(self, bilhete):
        """Confere bilhete com o número sorteado."""
        acertos = 0
        for n in bilhete:
            if n in self.sorteado:
                acertos += 1
                if acertos == self.qtdd_numeros:
                    print(f"Voce acertou, foram {s.sorteios} sorteios.\n"
                          f"Os números sorteados foram {s.sorteado}.\n"
                          f"O bilhete contemplado foi {bilhete}.")
                    exit()
 

if __name__ == '__main__':
    bilhetes = [
        # 10 numeros
        # [2, 8, 14, 35, 12, 59, 13, 18, 27, 44],
        # 9 numeros
        # [6, 12, 14, 32, 38, 54, 39, 40, 26],
        # 7 numeros
        # [2, 8, 14, 1, 16, 24, 13],
        # [5, 7, 15, 13, 47, 36, 27],
        # [23, 27, 42, 21, 38, 44, 43],
        # [34, 48, 1, 60, 20, 45, 21],
        # [6, 8, 12, 15, 25, 26, 18],
        # [1, 2, 34, 38, 44, 18, 57],
        # [23, 38, 37, 44, 52, 27, 6],
        # 15 números
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
        [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],
    ]
#    s = NumerosSorteados()
    s = NumerosSorteados(1, 25, 15)

    while True:
        s.sortear()
        for bilhete in bilhetes:
            s.conferir(bilhete)

