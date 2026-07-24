"""
Introdução ao empacotamento e desempacotamento
"""
# se não for utilizar o resto dos elementos é só chamar de _
resto: list[str]
_, _, nome, *resto = ['Maria', 'Helena', 'Luiz']
print(nome)
print(resto)
