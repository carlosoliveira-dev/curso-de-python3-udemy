"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""
# for letra in texto
texto = 'Luiz'  # iterável

iteratador = iter(texto)  # iterator .__iter__()

while True:
    try:
        letra = next(iteratador) # .__next__() método next do iterator
        print(letra)
    except StopIteration:
        print('acabou a iteração :)')
        break

# for letra in texto:
#     print(letra)