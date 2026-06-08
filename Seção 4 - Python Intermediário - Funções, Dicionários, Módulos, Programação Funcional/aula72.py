# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplicar(*args):
    t = 1
    for n in args:
        t *= n
    return t

numeros = 1, 2, 3, 4, 5

r = multiplicar(*numeros)

print(f'resultado: {r}, valor correto: {1*2*3*4*5}')

# Crie uma função que fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def par_impar(n):
    if n % 2 == 0:
        return f'{n} é par'
    return f'{n} é impar'

print(par_impar(2))