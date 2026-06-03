# Empacotamento e desempacotamento de dicionários
# invertendo valores usando desempacotamento
# a, b = 1, 2
# a, b = b, a
# print(a, b)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

# (a1, a2), (b1, b2) = pessoa.items()
# print(a1, a2)
# print(b1, b2)

# for chave, valor in pessoa.items():
#     print(chave, valor)


dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}

# desempacotamento de dicionários dentro de outro
pessoa_completa = {**pessoa, **dados_pessoa} # atualiza o dicionário 'pessoa' com os dados de 'dados_pessoa'
# print(pessoa_completa)


# args e kwargs
# *args (já vimos)
# **kwargs - keyword arguments (argumentos nomeados)


def mostro_argumentos_nomeados(*args, **kwargs):
    print('NÃO NOMEADOS:', args)
    print('NOMEADOS:')
    for chave, valor in kwargs.items():
        print(chave, valor)
    print()

mostro_argumentos_nomeados(10, 20, nome='Joana', qlq=123)
mostro_argumentos_nomeados(555, **pessoa_completa)

configuracoes = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}
mostro_argumentos_nomeados(**configuracoes)