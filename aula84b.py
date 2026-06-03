# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.

# Filtro de dados em list comprehension
produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]

# filtra os elementos que são menores que 5
# não inclui os elementos se a condição for verdadeira
lista = [n for n in range(10) if n < 5]
print(lista, end='\n\n')

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    # mapeamento(modificar valores do iterável e adicionar na nova lista)
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
    # filtro(se a condição for verdadeira não adicionar na nova lista)
    # o filtro sempre vem depois do for e não tem else
    if (produto['preco'] >= 20 and produto['preco'] * 1.05) > 10
]

print(*novos_produtos, sep='\n')