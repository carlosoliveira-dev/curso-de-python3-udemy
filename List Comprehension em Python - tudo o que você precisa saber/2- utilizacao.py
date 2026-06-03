def divisãoFn(x, y):
    return x / y


def multiplicaçãoFn(x, y):
    return x * y


def potenciaçãoFn(x, y):
    return x ** y


numeros = [1, 2, 3, 4, 5]
# mapeando a lista para outra lista
# chamando a função para cada item da lista
divisão = [divisãoFn(numero, 2) for numero in numeros]
multiplicação = [multiplicaçãoFn(numero, 2) for numero in numeros]
quadrado = [potenciaçãoFn(numero, 2) for numero in numeros]

print(numeros)
print(divisão)
print(multiplicação)
print(quadrado)
