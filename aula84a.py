# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.

# Mapeamento de dados em list comprehension
# mapeamento é fazer uma ação em cada elemento do iterável
produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]

mapeamento_original = [
    # crio um dicionário vazio {} em cada iteração
    # defino o nome das chaves e atribuo o valor do dicionário original
    {'nome': produto['nome'], 'preco': produto['preco']}
    for produto in produtos
] 

mapeamento_original_desempacotando = [
    # desempacoto um dicionário por vez em cada iteração
    {**produto}
    for produto in produtos
] 

novos_produtos = [
    # {} cria um novo dicionário vazio para cada item de produtos
    # 'preco': produto['preco'] cria uma chave 'preco' no novo dicionário e adiciona o valor de produto['preco']
    # * 1.05 aumenta o preço do produto em 5%
    {**produto, 'preco': produto['preco'] * 1.05} 
    if produto['preco'] > 20 else {**produto} # else retorne o dicionário inteiro
    for produto in produtos
]

# print(*mapeamento_original, sep='\n')

# print(*mapeamento_original_desempacotando, sep='\n')

print(*novos_produtos, sep='\n') # usamos um * só porque estamos desempacotando uma lista