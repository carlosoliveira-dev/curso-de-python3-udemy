'''
  como usar o arquivo __init__ em módulos python
  o arquivo __init__ permite tratar um package como se ele fosse um módulo
  disponibilizando funções e variáveis, basta importar o que quiser no __init__.py
'''
import aula99_package # isso é na verdade uma pasta

aula99_package.fala_oi()
print(aula99_package.soma_do_modulo(1, 2))
print(aula99_package.variavel)

print(aula99_package.c)