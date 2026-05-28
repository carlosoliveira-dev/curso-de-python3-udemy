"""
split e join com list e str
split - divide uma string (list)
join - une uma string
"""
frase = '   Olha só que   , coisa interessante          '
lista_frases_cruas = frase.split(',')

lista_frases = []
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip()) # .strip remove os espaços do começo e do fim da string

print(f'{lista_frases_cruas=}')
print(f'{lista_frases=}')
frases_unidas = ', '.join(lista_frases)
print(f'{frases_unidas=}')