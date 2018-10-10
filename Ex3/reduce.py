#!/usr/bin/env python

import sys

transacao = {}
for linha in sys.stdin:
    linha = linha.strip()

    ano, ocorrencia = linha.split('\t', 1)

    try:
        ocorrencia = int(ocorrencia)
    except ValueError:
        continue;

    try:
        transacao[ano] = transacao[ano] + ocorrencia
    except KeyError:
        transacao[ano] = ocorrencia

# Imprime o total por ano - ordenado pelo ano (nao pelas ocorrencias)
for ano in sorted(transacao.keys()):
    print("{}\t{}".format(ano, transacao[ano]))
