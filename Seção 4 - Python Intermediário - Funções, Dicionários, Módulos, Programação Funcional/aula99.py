'''
  diferentes formas de fazer a importação
  importar só o package(pasta) não tem muita utilidade
  por isso o ideal é importar o módulo dentro do package que vai usar

'''
from aula99_package.modulo import soma_do_modulo
from aula99_package import modulo
import aula99_package.modulo
from aula99_package.modulo import * # má prática de programação

from sys import path

print(__name__)
print(*path, sep='\n')
print(soma_do_modulo(1, 2))
print(aula99_package.modulo.soma_do_modulo(1, 2))
print(modulo.soma_do_modulo(1, 2))
print(variavel)
print(nova_variavel)