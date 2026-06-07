# Dictionary Comprehension e Set Comprehension
produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}

dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor
    in produto.items()
    if chave != 'categoria'
}

print('Dictionary Comprehension em produto', dc, end='\n\n')


lista = [
    ('a', 'valor a'),
    ('b', 'valor b'),
    ('c', 'valor c'),
]

# criando um novo dicionário a partir das tuplas dentro da lista
dc = {
    chave: valor
    for chave, valor in lista
}

print('convertendo lista usando Dictionary Comprehension', dc, end='\n\n')

# a classe dict consegue transformar em dicionário as listas que tem a mesma estrutura de um dicionário(chave, valor)
print('convertendo lista usando a classe dict', dict(lista))


# Set Comprehension 
# set's não garantem a ordem dos elementos 
s1 = {2 ** i for i in range(10)}
print('gerando um set com Set Comprehension', s1)