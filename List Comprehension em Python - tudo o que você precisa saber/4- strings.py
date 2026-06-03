string = 'Otávio Miranda'

numero_de_letras = 3

# o método join juntou todas as letras denovo
nova_string = ''.join([letra for letra in string])
print(nova_string)

# faz o fatiamento da string usando List Comprehension
nova_string = [
    string[indice:indice + numero_de_letras]
    for indice in range(0, len(string), numero_de_letras)
]

print(nova_string)

# adiciona um ponto em cada fatia da string
nova_string = '.'.join([
    # fatiamento da string (indice atual) : (indice atual + numero_de_letras) 
    string[indice:indice + numero_de_letras]
    for indice in range(0, len(string), numero_de_letras)
])

print(nova_string)
