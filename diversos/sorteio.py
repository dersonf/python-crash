from random import sample
from sys import exit


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
        # self._gera_estatisticas()

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
                # print(self.contemplados)
                for contemplado in self.contemplados:
                    print(contemplado)
                exit()
            # if self.sorteios < 10:
            # for bilhete in bilhetes:
            #     print(bilhete)
            # exit()
            # self._pega_os_15_maiores()
        elif acertos == 11:
            self.premios_11_pontos += 1
        elif acertos == 12:
            self.premios_12_pontos += 1
        elif acertos == 13:
            self.premios_13_pontos += 1
        elif acertos == 14:
            self.premios_14_pontos += 1

    # def _gera_estatisticas(self):
    #     """Gera estatística dos números sorteados."""
    #     for n in self.sorteado:
    #         if n not in self.vezes_sorteados.keys():
    #             self.vezes_sorteados[n] = 1
    #         else:
    #             self.vezes_sorteados[n] += 1

    # def _pega_os_15_maiores(self):
    #     """Pega os 15 primeiros mais sorteados."""
    #     posicao = 1
    #     for sorteado in range(15):
    #         maior = max(self.vezes_sorteados, key=self.vezes_sorteados.get)
    #         # print(f"O {posicao}º mais sorteado foi {maior}.")
    #         posicao += 1
    #         del self.vezes_sorteados[maior]
    #         self.sugestao.append(maior)
    #     self.sugestao.sort()
    #     bilhetes.append(self.sugestao)
    #     self._reinicia_estatistica()

    def _resumo(self):
        """Imprimi resumo statístico."""
        print(f"- Sorteios: {s.sorteios}.\n"
            #   f"- Números sorteados: {s.sorteado}.\n"
              f"- Prêmios 11 pontos: {self.premios_11_pontos}.\n"
              f"- Prêmios 12 pontos: {self.premios_12_pontos}.\n"
              f"- Prêmios 13 pontos: {self.premios_13_pontos}.\n"
              f"- Prêmios 14 pontos: {self.premios_14_pontos}.")
        if not self.contemplados:
            print(f"- Bilhete contemplado: 0.")
        else:
            print(f"- Bilhete contemplados: {self.contemplados[-1]}.")
        print(f"- Vezes contemplado: {len(self.contemplados)}.\n"
              f"- Total de bilhetes: {len(bilhetes)}.\n")
        # print(self.contemplados)
        self._reinicia_estatistica()


if __name__ == '__main__':
    bilhetes = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
        [1, 2, 3, 5, 6, 7, 8, 11, 15, 16, 19, 20, 21, 23, 24],
        [1, 2, 3, 5, 6, 8, 9, 11, 12, 16, 17, 19, 23, 24, 25],
        [1, 2, 3, 6, 8, 10, 11, 14, 17, 18, 19, 20, 22, 24, 25],
        [1, 2, 3, 7, 8, 9, 12, 14, 15, 18, 20, 21, 23, 24, 25],
        [1, 2, 7, 8, 9, 10, 12, 14, 15, 20, 21, 22, 23, 24, 25],
        [1, 3, 4, 5, 6, 8, 9, 10, 13, 14, 16, 22, 23, 24, 25],
        [1, 3, 4, 7, 8, 13, 15, 16, 18, 19, 21, 22, 23, 24, 25],
        [1, 3, 5, 6, 8, 9, 10, 13, 14, 15, 16, 18, 20, 21, 24],
        [1, 3, 6, 7, 8, 9, 10, 11, 13, 14, 16, 17, 20, 21, 25],
        [1, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 18, 20, 22, 23],
        [1, 6, 7, 8, 9, 10, 11, 12, 13, 17, 18, 19, 22, 24, 25],
        [2, 3, 4, 5, 7, 13, 15, 17, 18, 20, 21, 22, 23, 24, 25],
        [2, 3, 4, 5, 7, 8, 10, 11, 12, 13, 14, 17, 19, 21, 22],
        [2, 3, 5, 6, 7, 8, 9, 10, 11, 14, 15, 16, 17, 22, 25],
        [2, 3, 6, 7, 10, 13, 14, 15, 17, 18, 19, 21, 22, 23, 25],
        [2, 3, 6, 7, 8, 9, 11, 12, 13, 14, 15, 17, 19, 20, 24],
        [2, 3, 7, 8, 9, 12, 13, 14, 17, 18, 19, 21, 22, 23, 24],
        [2, 4, 5, 7, 9, 10, 11, 12, 15, 16, 17, 18, 20, 22, 25],
        [2, 4, 6, 8, 11, 14, 15, 16, 17, 18, 19, 20, 22, 23, 25],
        [2, 5, 6, 7, 10, 11, 12, 13, 15, 17, 19, 21, 22, 23, 25],
        [2, 5, 6, 7, 9, 11, 12, 13, 14, 16, 17, 20, 22, 24, 25],
        [3, 4, 5, 6, 9, 10, 12, 14, 17, 19, 20, 21, 23, 24, 25],
        [3, 4, 6, 7, 8, 9, 10, 11, 13, 17, 19, 20, 21, 23, 24],
        ]
#    s = NumerosSorteados()
    s = NumerosSorteados(1, 25, 15)

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
    # sorteios = 3_000_000
    # with open(filename, 'a') as f:
    #     for c in range(sorteios):
    #         s.sortear()
    #         f.write(f"{s.sorteado}\n")
