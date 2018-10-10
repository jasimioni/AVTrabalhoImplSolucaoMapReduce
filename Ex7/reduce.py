#!/usr/bin/env python

import sys

peso = {}
for linha in sys.stdin:
    linha = linha.strip()

    mercadoria, peso_tx = linha.split('\t', 1)

    try:
        peso_tx = int(peso_tx)
    except ValueError:
        continue;

    try:
        peso[mercadoria] = peso[mercadoria] + peso_tx
    except KeyError:
        peso[mercadoria] = peso_tx

# Determina o maior peso
max_peso = max(peso.values())

# Imprime as mercadorias com o peso somado igual ao maximo
for mercadoria in sorted(peso.keys()):
    if peso[mercadoria] == max_peso:
        print("{}\t{}".format(mercadoria, peso[mercadoria]))
