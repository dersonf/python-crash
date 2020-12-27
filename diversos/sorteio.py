from random import sample
from sys import exit
import json


class NumerosSorteados:
    """Sorteia numeros da loteria."""

    def __init__(self, inicio=1, fim=60, qtdd=6):
        """Inicializa classe de sorteio"""
        self.inicio = inicio
        self.fim = fim + 1
        self.qtdd_numeros = qtdd
        self.contemplados = []
        self._reinicia_estatistica()

    def _reinicia_estatistica(self):
        self.sorteios = 0
        self.vezes_sorteados = {}
        self.premios_11_pontos = 0
        self.premios_12_pontos = 0
        self.premios_13_pontos = 0
        self.premios_14_pontos = 0
        self.sugestao = []

    def sortear(self):
        """Sorteia numeros."""
        self.sorteado = sample(
            range(self.inicio, self.fim), k=self.qtdd_numeros
        )
        self.sorteado.sort()
        self.sorteios += 1

    def conferir(self, bilhete):
        """Confere bilhete com o número sorteado."""
        acertos = 0
        for numero in bilhete:
            if numero in self.sorteado:
                acertos += 1
        if acertos == self.qtdd_numeros:
            self.contemplados.append(bilhete)
            self._resumo()
            if len(self.contemplados) >= 100:
                for contemplado in self.contemplados:
                    print(contemplado)
                exit()
        elif acertos == 11:
            self.premios_11_pontos += 1
        elif acertos == 12:
            self.premios_12_pontos += 1
        elif acertos == 13:
            self.premios_13_pontos += 1
        elif acertos == 14:
            self.premios_14_pontos += 1

    def _resumo(self):
        """Imprimi resumo statístico."""
        print(f"- Sorteios: {s.sorteios}.\n"
              f"- Prêmios 11 pontos: {self.premios_11_pontos}.\n"
              f"- Prêmios 12 pontos: {self.premios_12_pontos}.\n"
              f"- Prêmios 13 pontos: {self.premios_13_pontos}.\n"
              f"- Prêmios 14 pontos: {self.premios_14_pontos}.\n"
              f"- Vezes contemplado: {len(self.contemplados)}.\n"
              f"- Total de bilhetes: {len(bilhetes)}.")
        if not self.contemplados:
            print(f"- Bilhete contemplado: 0.\n")
        else:
            print(f"- Bilhete contemplados: {self.contemplados[-1]}.\n")
        self._reinicia_estatistica()


if __name__ == '__main__':
    # bilhetes = []
    # s = NumerosSorteados()
    s = NumerosSorteados(1, 25, 15)

    filename = 'bilhetes.json'
    with open(filename) as f:
        dados = json.load(f)
        bilhetes = dados['teste001']

    # Loop de sorteios e conferencia
    while True:
        s.sortear()
        for bilhete in bilhetes:
            s.conferir(bilhete)

    # Um sorteio
    # s.sortear()
    # for bilhete in bilhetes:
    #     s.conferir(bilhete)
    # s._resumo()

    # Fazer varios sorteios
    # filename = 'sorteios.txt'
    # sorteios = 1_000
    # with open(filename, 'a') as f:
    #     for c in range(sorteios):
    #         s.sortear()
    #         f.write(f"{s.sorteado}\n")

# duas cartelas com 16 números não valem a pena
