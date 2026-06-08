# map, partial, GeneratorType e esgotamento de Iterators

from functools import partial
from types import GeneratorType


# map - para mapear dados
def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]


def aumentar_porcentagem(valor, porcentagem):
    return round(valor * porcentagem, 2)

'''
  função que retorna uma closure
  permite passar um argumento e pausar a função
  com o primeiro argumento salvo no escopo e depois
  executar quando quiser
  '''
aumentar_dez_porcento = partial(
    aumentar_porcentagem,
    porcentagem=1.1
)

# novos_produtos = [
#     {**p,
#         'preco': aumentar_dez_porcento(p['preco'])}
#     for p in produtos
# ]

'''
  recebe um produto por vez e faz o processamento
  return {} -> retorna um dicionário vazio
  **produto -> desempacota o dicionário dentro desse
  'preco': modifica o valor original da chave com um
  novo valor chamando aumentar_dez_porcento
'''
def muda_preco_de_produtos(produto):
    return {
        **produto,
        'preco': aumentar_dez_porcento(
            produto['preco'] # acessa o valor original do produto 
        )
    }

'''
  a função map precisa de outra função
  é essa função que vai fazer a tarefa
  e receber um item do iterável por vez
  e fazer o processamento
  converteu o map para lista porque map é um
  iterator e depois de esgotar não dá mais pra
  percorrer os item denovo, já na lista a gente
  consegue iterar quantas vezes quiser
'''
novos_produtos = list(map(
    muda_preco_de_produtos,
    produtos
))


print_iter(produtos)
print_iter(novos_produtos)

print(
    list(map(
        lambda x: x * 3,
        [1, 2, 3, 4]
    ))
)