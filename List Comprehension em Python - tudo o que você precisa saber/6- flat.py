# gera uma lista com o número e o número elevado ao quadrado
numeros = [[numero, numero ** 2] for numero in range(10)]

# pega todos os elementos de números e cria uma lista igual
exemplo1 = [x for x in numeros]
print(f'{exemplo1=}', end='\n\n')

"""
flat significa achatar(transformar em uma só lista)

1- numeros: É a sua lista original que contém várias sublistas (ex: [[1, 2], [3, 4]]).
2- for x in numeros: Percorre cada sublista x dentro da lista principal.
3- for y in x: Percorre cada elemento individual y dentro da sublista atual x.
4- y (no início): É o que será adicionado à nova lista flat.
"""
flat = [y for x in numeros for y in x]
print(numeros)
print(flat)
