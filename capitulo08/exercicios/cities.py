#!/usr/bin/python3


def describe_city(cidade, pais='brasil'):
    """Exibe o país em que está a cidade."""
    print(f"{cidade.title()} está no(a) {pais.title()}.")

describe_city('São Paulo')
describe_city('ceará')
describe_city('toronto', 'canadá')
