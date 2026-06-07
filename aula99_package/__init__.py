'''
  esse arquivo é executado quando qualquer coisa for importada de dentro
  desse package
  quando importamos algo em um módulo python ele automaticamente exporta tudo
  por padrão, permitindo a importação em qualquer outro módulo

  
  https://stackoverflow.com/questions/2386714/why-is-import-bad
'''
# tudo que for criado em modulo_b vai ficar disponível em aula99_package
from aula99_package.modulo_b import *

from aula99_package.modulo import soma_do_modulo, variavel

print('Você importou', __name__)
