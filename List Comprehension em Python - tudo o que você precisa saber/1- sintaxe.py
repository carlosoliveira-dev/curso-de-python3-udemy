numeros = [1, 2, 3, 4, 5]

# isso cria uma referência(não faz uma cópia da lista)
# se modificar a lista numeros vai modificar também a lista novos_numeros
# novos_numeros = numeros

# retorna uma cópia do objeto
# novos_numeros = numeros.copy()


# for numero in numeros:
#     novos_numeros.append(numero)

novos_numeros = [numero for numero in numeros]


numeros[0] = 20
print(novos_numeros)
