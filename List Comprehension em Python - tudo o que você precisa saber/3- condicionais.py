numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# isso é um filter porque seleciona itens da lista numeros e joga na nova lista
numeros_maiores_que_cinco = [n for n in numeros if n > 5]
impares = [n for n in numeros if n % 2 != 0]
pares = [n for n in numeros if n % 2 == 0]

se_for_6_vira_600 = [
    numero
    if numero != 6 else 600
    for numero in pares
]

print(f'{numeros=}')
print(f'{numeros_maiores_que_cinco=}')
print(f'{impares=}')
print(f'{pares=}')
print(f'{se_for_6_vira_600=}')
