"""Conta palavras mais comuns de um arquivo texto.

kalkuli_vortoj.py arg1
arg1 é um número inteiro que define as arg1 mais encontradas no texto
"""

import sys
from collections import Counter

try:
    nombro_da_vortoj = int(sys.argv[1])
except Exception as exc:
    print(exc)
    print('uzu: kalkuli_vortoj.py nombro_vortoj')
    sys.exit(1)

kalkulilo = Counter(vorto.lower()
                    for lineo in sys.stdin
                    for vorto in lineo.strip().split()
                    if vorto)

for vorto, kalkuli in kalkulilo.most_common(nombro_da_vortoj):
    sys.stdout.write(str(kalkuli))
    sys.stdout.write("\t")
    sys.stdout.write(f'{vorto}')
    sys.stdout.write("\n")
