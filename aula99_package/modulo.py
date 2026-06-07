'''
  todas as importações tem que ser feitas do ponto de vista da raiz do projeto
  onde está o arquivo __main__ que vai usar os imports
  todas as importações do programa devem ser relativas ao arquivo __main__
  e elas não vão funcionar nos outros módulos
  execute esse módulo para testar,
  isso irá gerar uma exceção: ModuleNotFoundError: No module named 'aula99_package'
  porque esse módulo foi feito para ser importado pelo __main__, e não foi feito para ser
  executado sozinho
'''
from aula99_package.modulo_b import fala_oi

'''
  quando a pessoa usar import *
  a gente define o que vai ser exportado pro módulo __main__
  caso o nome da função ou variável não estiver nessa lista
  o __main__ não vai executar
  caso não modificar a variável __all__ tudo o que tiver no módulo
  vai ser exportado por padrão
'''
__all__ = [
    'variavel',
    'soma_do_modulo',
    'nova_variavel',
]

variavel = 'Alguma coisa'


def soma_do_modulo(x, y):
    return x + y


nova_variavel = 'OK'