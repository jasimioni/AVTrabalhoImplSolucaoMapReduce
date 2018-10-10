#!/usr/bin/env python

import sys

sys.stdin.readline() # Remove a primeira linha para nao incluir o cabecalho na conta

for linha in sys.stdin:
    linha = linha.strip()
    palavras = linha.split(";")
    print("{}\t{}".format(palavras[1], "1"))

