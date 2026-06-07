'''
  Modularização - Entendendo os seus próprios módulos Python
  O primeiro módulo executado chama-se __main__
  Você pode importar outro módulo inteiro ou parte do módulo
  O python conhece a pasta onde o __main__ está e as pastas
  abaixo dele.
  Ele não reconhece pastas e módulos acima do __main__ por
  padrão
  O python conhece todos os módulos e pacotes presentes
  nos caminhos de sys.path
'''

import aula97a_m
from aula97a_m import soma, variavel_modulo

print('Este módulo se chama', __name__)

# duas formas de acessar variáveis de um módulo
print(aula97a_m.variavel_modulo)
print(variavel_modulo)

# duas formas de acessar funções de um módulo
print(soma(2, 3))
print(aula97a_m.soma(2, 3))