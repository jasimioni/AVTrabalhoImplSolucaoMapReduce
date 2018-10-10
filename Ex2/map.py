#!/usr/bin/env python

import sys

for linha in sys.stdin:
    linha = linha.strip()
    palavras = linha.split(";")
    if palavras[0] == 'Brazil':
        print("{}\t{}".format(palavras[3], "1"))

