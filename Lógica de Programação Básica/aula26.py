"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
"""
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel:->10}')
print(f'{variavel:-<10}.')
print(f'{variavel:-^10}.')
'''
Decomposição do Formato: :0=+10,.1f
Aqui está o que cada caractere dentro do especificador de formato faz, da esquerda para a direita:
0 (Preenchimento com zeros): Indica que, se o número for menor que a largura definida, ele deve ser
    preenchido com zeros à esquerda (após o sinal).
= (Alinhamento com sinal): Força o sinal (+ ou -) a ficar na extrema esquerda, permitindo que o 
    preenchimento com zeros ocorra entre o sinal e o número.
+ (Força o sinal): Garante que o sinal (+ para positivos, - para negativos) seja sempre exibido.
10 (Largura mínima): Define que a string resultante terá, no mínimo, 10 caracteres de largura total.
, (Separador de milhar): Adiciona uma vírgula como separador de milhares.
.1f (Precisão): Define que o número deve ser exibido como um float com exatamente 1 dígito 
    após a vírgula (o número é arredondado).
'''
print(f'{1000.4873648123746:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08X}')
print(f'{variavel!r}')