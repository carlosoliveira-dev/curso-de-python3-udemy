'''
    namedtuples - tuplas imutáveis com nomes para valores
    Usamos namedtuples para criar classes de objetos que são apenas um
    agrupamento de atributos, como classes normais sem métodos, ou registros de
    bases de dados, etc.
    As namedtuples são imutáveis assim como as tuplas.
    https://docs.python.org/3/library/collections.html#collections.namedtuple
    https://docs.python.org/3/library/typing.html#typing.NamedTuple
    https://brasilescola.uol.com.br/curiosidades/baralho.htm
    from collections import namedtuple
'''
from typing import NamedTuple


class Carta(NamedTuple):
    valor: str = 'VALOR'
    naipe: str = 'NAIPE'


as_espadas = Carta('A', 'ESPADAS')

print('dicionário:', as_espadas._asdict())
print(as_espadas)

# em uma tupla comum chamaria pelo índice
print('acessa elemento pelo índice:', as_espadas[0])
# usando NamedTuple fica mais legível
print('acessa elemento pelo atributo:', as_espadas.valor)

print('acessa o NAIPE pelo índice:', as_espadas[1])
print('acessa o NAIPE pelo atributo:', as_espadas.naipe)

print()
print('campos da NamedTuple:', as_espadas._fields)
print('valores default da NamedTuple:', as_espadas._field_defaults)
print()

print('elementos da NamedTuple:')
for valor in as_espadas:
    print(valor)
