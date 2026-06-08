'''
Exercício - Unir listas
Crie uma função zipper (como o zipper de roupas)
O trabalho dessa função será unir duas
listas na ordem.
Use todos os valores da menor lista.
Ex.:
['Salvador', 'Ubatuba', 'Belo Horizonte']
['BA', 'SP', 'MG', 'RJ']
Resultado
[('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]
'''
# minha implementação do exercício
lista1 = ['Salvador', 'Ubatuba', 'Belo Horizonte', 'Rio de Janeiro', 'Rio Grande do Sul']
lista2 = ['BA', 'SP', 'MG', 'RJ', 'RS']

def unir_listas(l1, l2):
    nova_lista = []

    if len(l1) > len(l2):
        print('lista 1 é maior')
        for i, valor in enumerate(l2):
            nova_lista.append((l1[i], l2[i]))
    elif len(l1) == len(l2):
        print('listas do mesma tamanho')
        for i, valor in enumerate(l1):
            nova_lista.append((l1[i], l2[i]))
    else:
        print('lista 2 é maior')
        for i, valor in enumerate(l1):
            nova_lista.append((l1[i], l2[i]))
    return nova_lista

r = unir_listas(lista1, lista2)
print(r)
