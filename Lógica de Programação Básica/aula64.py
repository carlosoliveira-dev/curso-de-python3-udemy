# validador de cpfs
import sys
import random

# cálculo do primeiro dígito do cpf
print('Cálculo do primeiro dígito do CPF')
cpf_nove_digitos = ''
for i in range(0, 9):
    cpf_nove_digitos += str(random.randint(0, 9))
print(cpf_nove_digitos)
contagem = 10
lista_soma = []
for digito in cpf_nove_digitos:
    digito = int(digito)
    lista_soma.append(digito * contagem)
    contagem -= 1
print(lista_soma)
somado = 0
for valor in lista_soma:
    somado += valor
somado *= 10
print(somado)
resto = somado % 11
print(resto)
primeiro_digito = 0
if resto > 9:
    primeiro_digito = 0
    print(f'{primeiro_digito=}')
else:
    primeiro_digito = resto
    print(f'{primeiro_digito=}')
print()
# cálculo do segundo dígito do cpf
print('Cálculo do segundo dígito do CPF')
cpf_dez_digitos = cpf_nove_digitos + str(primeiro_digito)
contagem = 11
lista_soma = []
for digito in cpf_dez_digitos:
    digito = int(digito)
    lista_soma.append(digito * contagem)
    contagem -= 1
print(lista_soma)
somado = 0
for valor in lista_soma:
    somado += valor
somado *= 10
print(somado)
resto = somado % 11
print(resto)
segundo_digito = 0
if resto > 9:
    segundo_digito = 0
    print(f'{segundo_digito=}')
else:
    segundo_digito = resto
    print(f'{segundo_digito=}')
cpf_gerado_pelo_calculo = f'{cpf_nove_digitos}{primeiro_digito}{segundo_digito}'

print(f'{cpf_gerado_pelo_calculo=}')
    