"""
    Iterando strings com while
"""

nome = 'Carlos Júnior Torres de Oliveira'
contador = 0

while contador < len(nome):
    print(f'{nome[contador]}-', end='')
    contador += 1