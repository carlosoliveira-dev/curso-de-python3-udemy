linhas_e_colunas = [
    (x, y) # gerando uma tupla com x e y
    if y != 2 else (x, y * 1000)
    for x in range(1, 11)
    for y in range(1, 6)
    if x != 1 # só aceita o valor de x que for diferente de 1
]

print(*linhas_e_colunas, sep='\n')
