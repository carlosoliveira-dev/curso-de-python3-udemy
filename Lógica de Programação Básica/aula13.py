# Aula 13 - f-strings
nome = 'Carlos'
altura = 1.70
peso = 55.500
imc = peso / altura ** 2
oi = ... # Ellipsis é um place holder para um código ainda não escrito.
print(oi)
linha_1 = f'nome: {nome}' # f-string é uma string que tem um f no início e permite colocar expressões dentro de chaves {}.
print(linha_1)
print(f'altura: {altura:.2f}') # :.2f formata o número com 2 casas decimais.
print(f'peso: {peso}')
print(f'Meu índice de massa corporal é: {imc:.2f}')