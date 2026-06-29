import enum

''' declarando o enum dessa forma não tem autocompletar no vs code '''
# Direcoes = enum.Enum('Direcoes', ['ESQUERDA', 'DIREITA'])


class Direcoes(enum.Enum):
    ESQUERDA = enum.auto()
    DIREITA = enum.auto()
    ACIMA = enum.auto()
    ABAIXO = enum.auto()


# 3 formas de retornar o membro inteiro
print(Direcoes(1), Direcoes['ESQUERDA'], Direcoes.ESQUERDA)

# retornando a chave do membro
print(Direcoes(1).name, Direcoes['ESQUERDA'].name, Direcoes.ESQUERDA.name)

# retornando o valor do membro
print(Direcoes(1).value, Direcoes['ESQUERDA'].value, Direcoes.ESQUERDA.value)


def mover(direcao: Direcoes):
    if not isinstance(direcao, Direcoes):
        raise ValueError('Direção não encontrada')

    print(f'Movendo para {direcao.name} ({direcao.value})')


mover(Direcoes.ESQUERDA)
mover(Direcoes.DIREITA)
mover(Direcoes.ACIMA)
mover(Direcoes.ABAIXO)
mover(Direcoes.DIREITA)
