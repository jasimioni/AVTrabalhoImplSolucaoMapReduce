#!/usr/bin/env python

import sys

peso = {}
for linha in sys.stdin:
    linha = linha.strip()

    ano, mercadoria, peso_tx = linha.split('\t')
    if not ano in peso.keys(): # Inicializa o primeiro nivel da Hash
        peso[ano] = {}

    try:
        peso_tx = int(peso_tx)
    except ValueError:
        continue;

    try:
        peso[ano][mercadoria] = peso[ano][mercadoria] + peso_tx
    except KeyError:
        peso[ano][mercadoria] = peso_tx


for ano in sorted(peso.keys()):
    # Determina o maior peso
    max_peso = max(peso[ano].values())

    # Imprime as mercadorias com o peso somado igual ao maximo
    for mercadoria in peso[ano].keys():
        if peso[ano][mercadoria] == max_peso:
            print("{}\t{}\t{}".format(ano, mercadoria, peso[ano][mercadoria]))
