#!/usr/bin/env python

import sys

sys.stdin.readline() # Remove a primeira linha para nao incluir o cabecalho na conta

# Sequencia: [ pais, ano, codigo, mercadoria, fluxo, valor, peso, unidade, quantidade, categoria ]

for linha in sys.stdin:
    linha = linha.strip()
    palavras = linha.split(";")
    if palavras[6] == '': # Corrige para que linhas sem itens vire zero
        palavras[6] = 0
    print("{}\t{}\t{}".format(palavras[1], palavras[3], palavras[6])) 

