#!/usr/bin/env python

import sys

transacao = {}
for linha in sys.stdin:
    linha = linha.strip()

    pais, ocorrencia = linha.split('\t', 1)

    try:
        ocorrencia = int(ocorrencia)
    except ValueError:
        continue;

    try:
        transacao[pais] = transacao[pais] + ocorrencia
    except KeyError:
        transacao[pais] = ocorrencia

# Determina a maior ocorrencia
max_tx = max(transacao.values())

# Imprime todos os paises que tem essa ocorrencia
for pais in transacao.keys():
    if transacao[pais] == max_tx:
        print("{}\t{}".format(pais, transacao[pais]))
