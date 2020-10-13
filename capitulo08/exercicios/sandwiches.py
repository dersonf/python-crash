#!/usr/bin/python3


def colocar_no_sandwiche(*recheios):
    if len(recheios) == 1:
        print(f"\nO sandwiche terá o ingrediente:")
        for recheio in recheios:
            print(f"- {recheio}")
    else:
        print(f"\nO sandwiche terá os ingredientes:")
        for recheio in recheios:
            print(f"- {recheio}")

colocar_no_sandwiche('mortadela')
colocar_no_sandwiche('presunto', 'queijo')
colocar_no_sandwiche('carne', 'queijo', 'molho de tomate')
