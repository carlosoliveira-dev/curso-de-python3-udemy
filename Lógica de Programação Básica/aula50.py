
"""
Exercício
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz
"""
lista = ['Maria', 'Helena', 'Luiz', 'Carlos', 'Eliane', 'Cassiano', 'Júnior']
lista.append('João')

indices = range(len(lista)) # cria os índices de forma dinâmica

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))