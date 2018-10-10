#!/usr/bin/env python

import sys

sys.stdin.readline() # Remove a primeira linha para nao incluir o cabecalho na conta

# Sequencia: [ pais, ano, codigo, mercadoria, fluxo, valor, peso, unidade, quantidade, categoria ]

for linha in sys.stdin:
    linha = linha.strip()
    palavras = linha.split(";")
    if int(palavras[1]) == 2016:
        print("{}\t{}".format(palavras[3], "1")) 

