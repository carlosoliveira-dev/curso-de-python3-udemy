lista = []
for x in range(3):
    for y in range(3):
        lista.append((x, y))
# print(lista)

lista = [
    (x, y) # valores a serem incluidos
    for x in range(3)
    for y in range(3)
]
# print(lista)

lista = [
    # List comprehension dentro do valor gerado para uma nova lista 
    [(x, letra) for letra in 'Luiz'] # gerando uma nova lista
    for x in range(3) # para cada x
]

print(lista)