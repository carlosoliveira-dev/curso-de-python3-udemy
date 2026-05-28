"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
qtd_linhas = 7
qtd_colunas = 7

contador = 0
linha = 1
while linha <= qtd_linhas:
    coluna = 1
    while coluna <= qtd_colunas:
        contador +=1
        print(f'{linha=} {coluna=}')
        coluna += 1
    linha += 1
print(f'{contador=}')


print('Acabou')

# qtd_linhas = 5
# qtd_colunas = 5

# linha = 1
# while linha <= qtd_linhas:
#     coluna = 1
#     while coluna <= qtd_colunas:
#         print(f'{linha=} {coluna=}')
#         coluna += 1
#     linha += 1


# print('Acabou')