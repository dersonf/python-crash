from random import sample
from sys import exit
from plotly.graph_objs import Bar, Layout
from plotly import offline


class NumerosSorteados:
    """Sorteia numeros da loteria."""

    def __init__(self, inicio=1, fim=60, qtdd=6):
        """Inicializa classe de sorteio"""
        self.inicio = inicio
        self.fim = fim + 1
        self.qtdd_numeros = qtdd
        self._reinicia_estatistica()

    def _reinicia_estatistica(self):
        self.sorteios = 0
        self.vezes_sorteados = {}
        self.premios_menores = 0
        self.sugestao = []

    def sortear(self):
        """Sorteia numeros."""
        self.sorteado = sample(
            range(self.inicio, self.fim), k=self.qtdd_numeros
        )
        self.sorteios += 1
        self._gera_estatisticas()

    def conferir(self, bilhete):
        """Confere bilhete com o número sorteado."""
        acertos = 0
        for n in bilhete:
            if n in self.sorteado:
                acertos += 1
        if acertos == self.qtdd_numeros:
            self._resumo()
            if self.sorteios < 10:
                for bilhete in bilhetes:
                    print(bilhete)
                exit()
            self._pega_os_15_maiores()
        elif acertos >= 11:
            self.premios_menores += 1

    def _gera_estatisticas(self):
        """Gera estatística dos números sorteados."""
        for n in self.sorteado:
            if n not in self.vezes_sorteados.keys():
                self.vezes_sorteados[n] = 1
            else:
                self.vezes_sorteados[n] += 1

    def _pega_os_15_maiores(self):
        """Pega os 15 primeiros mais sorteados."""
        posicao = 1
        for sorteado in range(15):
            maior = max(self.vezes_sorteados, key=self.vezes_sorteados.get)
            # print(f"O {posicao}º mais sorteado foi {maior}.")
            posicao += 1
            del self.vezes_sorteados[maior]
            self.sugestao.append(maior)
        self.sugestao.sort()
        bilhetes.append(self.sugestao)
        self._reinicia_estatistica()

    def _resumo(self):
        """Imprimi resumo statístico."""
        print(f"- Sorteios: {s.sorteios}.\n"
              f"- Números sorteados: {s.sorteado}.\n"
              f"- Prêmios menores: {self.premios_menores}.\n"
              f"- Bilhete contemplado: {bilhete}.\n"
              f"- Total de bilhetes: {len(bilhetes)}.\n")
        print(bilhetes)


if __name__ == '__main__':
    bilhetes = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
        [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],
        [1, 2, 3, 4, 5, 6, 7, 8, 19, 20, 21, 22, 23, 24, 25],
        [3, 4, 6, 7, 9, 10, 12, 13, 14, 15, 16, 17, 20, 22, 23],
        [1, 3, 6, 8, 9, 11, 12, 14, 15, 16, 17, 19, 20, 21, 22],
        [2, 4, 5, 6, 7, 11, 13, 16, 17, 18, 19, 20, 21, 22, 23],
        [3, 4, 5, 6, 7, 8, 13, 14, 15, 18, 20, 22, 23, 24, 25],
        [1, 3, 4, 6, 8, 10, 12, 13, 16, 17, 21, 22, 23, 24, 25],
        [3, 4, 5, 8, 9, 10, 12, 13, 14, 15, 17, 20, 22, 23, 25],
        [4, 8, 10, 11, 12, 13, 14, 15, 16, 18, 19, 22, 23, 24, 25],
        [1, 2, 3, 4, 5, 6, 8, 9, 11, 14, 15, 16, 19, 23, 24],
        [2, 3, 6, 8, 9, 10, 11, 13, 14, 15, 16, 18, 20, 23, 25],
        [2, 3, 4, 7, 8, 9, 10, 11, 12, 13, 14, 18, 22, 23, 25],
        [1, 5, 6, 7, 9, 10, 13, 14, 16, 17, 18, 19, 21, 24, 25],
        [3, 6, 8, 9, 10, 11, 12, 14, 15, 16, 19, 21, 22, 24, 25],
        [1, 2, 3, 4, 7, 8, 10, 11, 14, 16, 17, 20, 22, 23, 25],
        [2, 3, 4, 5, 6, 7, 10, 11, 12, 13, 16, 18, 20, 24, 25],
        [2, 5, 6, 7, 9, 11, 12, 13, 16, 17, 18, 20, 22, 23, 25],
        [1, 2, 5, 6, 7, 8, 10, 13, 14, 18, 19, 20, 21, 23, 24],
        [1, 2, 3, 4, 5, 11, 12, 14, 17, 18, 19, 20, 22, 24, 25],
        [1, 3, 4, 6, 11, 12, 14, 15, 16, 18, 21, 22, 23, 24, 25],
        [2, 3, 4, 5, 7, 10, 12, 15, 18, 19, 21, 22, 23, 24, 25],
        [1, 2, 4, 6, 7, 8, 9, 10, 11, 15, 17, 18, 19, 20, 22],
        [1, 2, 3, 6, 10, 11, 13, 17, 18, 19, 20, 21, 22, 23, 24],
        [2, 5, 9, 11, 12, 13, 14, 15, 16, 18, 20, 21, 22, 23, 24],
        [1, 2, 3, 4, 7, 8, 9, 10, 11, 13, 14, 15, 17, 18, 24],
        [1, 2, 5, 6, 10, 11, 13, 14, 16, 17, 18, 19, 20, 21, 22],
        [1, 4, 6, 7, 8, 10, 11, 12, 15, 16, 17, 19, 20, 21, 22],
        [1, 2, 3, 4, 5, 6, 7, 10, 11, 12, 14, 16, 17, 19, 22],
        [1, 2, 4, 5, 6, 7, 9, 10, 12, 14, 15, 16, 21, 22, 24],
        [1, 2, 3, 4, 7, 9, 10, 12, 14, 16, 17, 20, 21, 23, 25]
        ]
#    s = NumerosSorteados()
    s = NumerosSorteados(1, 25, 15)

    while True:
        s.sortear()
        for bilhete in bilhetes:
            s.conferir(bilhete)



[3, 4, 6, 7, 9, 10, 12, 13, 14, 15, 16, 17, 20, 22, 23],
[1, 3, 6, 8, 9, 11, 12, 14, 15, 16, 17, 19, 20, 21, 22],
[2, 4, 5, 6, 7, 11, 13, 16, 17, 18, 19, 20, 21, 22, 23],
[3, 4, 5, 6, 7, 8, 13, 14, 15, 18, 20, 22, 23, 24, 25]