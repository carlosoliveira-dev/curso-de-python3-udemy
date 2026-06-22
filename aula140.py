# Herança Múltipla - Python Orientado a Objetos
# Quer dizer que no Python, uma classe pode estender
# várias outras classes.
# Herança simples:
# Animal -> Mamifero -> Humano -> Pessoa -> Cliente
# Herança múltipla e mixins
# mixin é uma classe que não faz parte daquela família -> Cliente(Pessoa, FileLog)
# Log -> FileLog
# Animal -> Mamifero -> Humano -> Pessoa -> Cliente
# Cliente(Pessoa, FileLog)


# Problema do diamante
# A, B, C, D
# D(B, C) - C(A) - B(A) - A
#
# método -> falar
# existe em A, em B e em C
#           A
#         /   \
#        B     C
#         \   /
#           D
# O python precisa decidir como chamar o método falar.
# Ele vai procurar em B ou em C?
# Qual a ordem de chamada nesse caso?

# Python 3 usa C3 superclass linearization
# para gerar o mro(Method Resolution Order).
# Você não precisa estudar isso (é complexo)
# https://en.wikipedia.org/wiki/C3_linearization
#
# Para saber a ordem de chamada dos métodos
# Use o método de classe Classe.mro()
# Ou o atributo __mro__ (Dunder - Double Underscore)