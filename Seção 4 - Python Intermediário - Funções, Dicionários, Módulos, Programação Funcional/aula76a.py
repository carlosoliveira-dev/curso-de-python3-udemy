
# Manipulando chaves e valores em dicionários
pessoa = {}

##
##

chave = 'nome' # essa chave dinâmica pode ser modificada

pessoa[chave] = 'Luiz Otávio'
pessoa['sobrenome'] = 'Miranda'


print(pessoa[chave])

pessoa[chave] = 'Maria'

del pessoa['sobrenome']
print(pessoa)
print(pessoa['nome'])

# print(pessoa.get('sobrenome')) # retorna None porque a chave não existe
if pessoa.get('sobrenome') is None:
    print('NÃO EXISTE')
else:
    print(pessoa['sobrenome'])

# print('ISSO Não vai') # se não tivesse essa verificação acima esse código não seria executado
