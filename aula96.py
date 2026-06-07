''' 
  Módulos padrão do Python (import, from, as e *)
  https://docs.python.org/3/py-modindex.html
  inteiro - import nome_modulo # importar o módulo inteiro não muda em nada a performance
  Vantagens: você tem o namespace do módulo
  Desvantagens: nomes grandes
'''
# import sys
# sys.exit() # sai do programa nessa linha de código
# platform = sys.platform
# print('Minha Plataforma:', platform)


'''
  partes - from nome_modulo import objeto1, objeto2
  Vantagens: nomes pequenos
  Desvantagens: Sem o namespace do módulo, se a gente sobrescrever a variável, não vai ter mais acesso a função original
'''
# from sys import exit, platform
# platform = 'sobrescrevi essa variável sem querer :('
# def exit():
#     print('Ha ha não vou finalizar o sistema ;)')
# print(platform)
# exit()


'''
  alias 1 - import nome_modulo as apelido
'''
# import sys as s
# sys = 'sobrescrevi o módulo sys'
# print(s.platform)
# print(sys)


'''
  alias 2 - from nome_modulo import objeto as apelido
  Vantagens: você pode reservar nomes para seu código
  Desvantagens: pode ficar fora do padrão da linguagem
'''
# from sys import platform as pf
# from sys import exit as ex
# print(pf)


'''
  má prática - from nome_modulo import *
  importa tudo de um módulo
  se precisar de uma coisa importa só ela
'''
from sys import platform, exit
print(platform)
exit()
print('PROGRAMA FINALIZOU, NEM VAI EXECUTAR ESSA LINHA')