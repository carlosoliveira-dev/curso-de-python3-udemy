"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""

import re
import sys

# cálculo do primeiro dígito do cpf
print('Cálculo do primeiro dígito do CPF')
# cpf = '746.824.890-70' \
#     .replace('.', '') \
#     .replace('-', '')
entrada = input('Digite o CPF[746.824.890-70]: ')
if entrada == entrada[0] * len(entrada):
    print('CPF inválido')
    sys.exit()
cpf = re.sub(
    r'[^0-9]',
    '',
    entrada
)
print(f'CPF depois da expressão regular: {cpf=}')
cpf_nove_digitos = cpf[:9]
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
if cpf == cpf_gerado_pelo_calculo:
    print(f'{cpf=} é válido')
else:
    print(f'{cpf=} é inválido')
    