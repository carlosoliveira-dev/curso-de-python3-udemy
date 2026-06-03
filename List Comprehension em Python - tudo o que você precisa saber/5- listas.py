nomes = ['luiz', 'maria', 'helena', 'joana', 'felipe']

# remove a última letra do nome
print('última letra removida:', nomes[0][:-1])

# imprime a última letra do nome
print('só a última letra:', nomes[0][-1])

# remove a última letra do nome
# adiciona a última letra mudando para maiúscula
novos_nomes = [
    f'{nome[:-1].lower()}{nome[-1].upper()}'
    for nome in nomes
]
print(f'{novos_nomes}')


# adiciona a primeira letra mudando para maiúscula
# adiciona o restante do nome
novos_nomes = [
    f'{nome[0].upper()}{nome[1:].lower()}'
    for nome in nomes
]

print(f'{novos_nomes}')

