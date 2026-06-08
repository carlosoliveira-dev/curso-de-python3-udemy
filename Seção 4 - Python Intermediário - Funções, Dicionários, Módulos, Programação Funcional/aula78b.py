# Métodos úteis em sets:
# use o debug para ver as alterações no set 
# add, update, clear, discard
s1 = set()
s1.add('Luiz')
s1.add(1)
s1.update(('Olá mundo', 1, 2, 3, 4))
s1.update('xyz') # vai iterar e adicionar cada item de forma separada
# s1.clear()
s1.discard('Olá mundo')
s1.discard('Luiz')
print(s1)

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos