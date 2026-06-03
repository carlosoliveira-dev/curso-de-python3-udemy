# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.
# print(list(range(10)))
lista = []
for numero in range(10):
    lista.append(numero)
print(lista)

# inclui item * 2 para cada item em um range de 10 valores
# ESQUERDA: o que eu quiser fazer com o item 
# DIREITA: passar o iterável
lista = [ item * 2 for item in range(10) ]
print(lista)

lista = [ letra * 3 for letra in ['a', 'b', 'c', 'd', 'e']]
print(lista)
