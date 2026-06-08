'''
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:

Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.

Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]

=================== resultado
lista_soma  = [2, 4, 6, 8]
'''

# minha implementação
lista_a = [10, 23, 3, 40, 5, 6, 7]
lista_b = [1, 2, 3, 4]
lista_soma = []

maximo = min(len(lista_a), len(lista_b))

for i in range(maximo):
    lista_soma.append(lista_a[i] + lista_b[i])

print('minha implementação:', lista_soma)

# implementação mais pythonica
lista_soma = [ x + y for x, y in zip(lista_a, lista_b) ]
print('implentação pythonica:', lista_soma)


# implementação mais completa
from itertools import zip_longest

lista_a = [10, 2, 3, 4, 5]
lista_b = [12, 2, 3, 6, 50, 60, 70]
lista_soma = [x + y for x, y in zip_longest(lista_a, lista_b, fillvalue=0)]
print('implementação mais completa:', lista_soma)