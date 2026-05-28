"""
Flag (Bandeira) - Marcar um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade
"""

# v1 = 'a' # v1 recebe o valor 'a' e aponta para um local na memória onde esse valor está armazenado
# v2 = 'a' # v2 recebe o valor 'a' e aponta para o mesmo local na memória onde o valor 'a' está armazenado, pois strings são imutáveis e Python otimiza o uso de memória reutilizando objetos imutáveis com o mesmo valor
# v3 = 'b' # v3 recebe o valor 'b' e aponta para um local diferente na memória onde esse valor está armazenado, pois 'b' é um valor diferente de 'a'

# print(f'{v1=}, id dessa variável: {id(v1)}')
# print(f'{v2=}, id dessa variável: {id(v2)}')
# print(f'{v3=}, id dessa variável: {id(v3)}')

condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True # é ruim declarar para usar fora do bloco
    print('Faça algo')
else:
    print('Não faça algo')


if passou_no_if is None:
    print('Não passou no if')
else:
    print('Passou no if')

print(passou_no_if, passou_no_if is None)
print(passou_no_if, passou_no_if is not None)
