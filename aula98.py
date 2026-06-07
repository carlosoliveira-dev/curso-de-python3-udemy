'''
  os módulos são singletons o que quer dizer que se tentar importar várias vezes
  do modo tradicional, não vai recarregar o módulo
  para fazer isso podemos usar o importlib do python
  podemos usar essa biblioteca no modo iterativo do python
  para recarregar o módulo sem precisar sair do terminal
'''
import importlib

import aula98_m

print(aula98_m.variavel)

for i in range(10):
    importlib.reload(aula98_m) # recarrega o módulo em cada iteração
    print(i)

print('Fim')