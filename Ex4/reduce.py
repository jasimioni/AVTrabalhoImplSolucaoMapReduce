#!/usr/bin/env python

import sys

transacao = {}
for linha in sys.stdin:
    linha = linha.strip()

    mercadoria, ocorrencia = linha.split('\t', 1)

    try:
        ocorrencia = int(ocorrencia)
    except ValueError:
        continue;

    try:
        transacao[mercadoria] = transacao[mercadoria] + ocorrencia
    except KeyError:
        transacao[mercadoria] = ocorrencia

# Determina a maior quantidade de transacoes
max_tx = max(transacao.values())

# Imprime as mercadorias com o numero igual maximo
for mercadoria in sorted(transacao.keys()):
    if transacao[mercadoria] == max_tx:
        print("{}\t{}".format(mercadoria, transacao[mercadoria]))
