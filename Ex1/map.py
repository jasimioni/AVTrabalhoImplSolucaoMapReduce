#!/usr/bin/env python

import sys

for linha in sys.stdin:
    linha = linha.strip()
    palavras = linha.split(";")
    print("{}\t{}".format(palavras[0], "1"))

