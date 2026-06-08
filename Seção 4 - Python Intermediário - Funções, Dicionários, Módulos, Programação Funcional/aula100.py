# copy, sorted, produtos.sort
'''
  o ideal é sempre fazer a cópia antes de fazer o processamento de dados
  porque a gente corre um sério risco de alterar os dados reais sem perceber
'''

# Exercícios
# minha implementação
import copy

from dados import produtos

# Aumente os preços dos produtos a seguir em 10%
produtos = [
    {**produto, 'preco': produto['preco'] * 1.10}
     for produto in produtos
]

# Gere novos_produtos por deep copy (cópia profunda)
novos_produtos = copy.deepcopy(produtos)
print('Aumente os preços dos produtos a seguir em 10%')
print(*novos_produtos, sep='\n')
print()

# Ordene os produtos por nome decrescente (do maior para menor)
print('Ordene os produtos por nome decrescente (do maior para menor)')
novos_produtos = sorted(novos_produtos, key=lambda item: item['nome'], reverse=True)

# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
produtos_ordenados_por_nome = copy.deepcopy(novos_produtos)
print(*produtos_ordenados_por_nome, sep='\n')
print()

# Ordene os produtos por preco crescente (do menor para maior)
novos_produtos = sorted(novos_produtos, key=lambda item: item['preco'])

# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
print('Ordene os produtos por preco crescente (do menor para maior)')
produtos_ordenados_por_preco = copy.deepcopy(novos_produtos)
print(*produtos_ordenados_por_preco, sep='\n')
