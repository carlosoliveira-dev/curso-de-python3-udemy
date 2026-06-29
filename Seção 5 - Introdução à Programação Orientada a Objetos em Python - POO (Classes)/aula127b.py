# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.

# minha implementação
# import json


# from aula127a import Pessoa


# with open('aula127.json', 'r', encoding='utf8') as arquivo:
#     dados_pessoa = json.load(arquivo)
#     p1 = Pessoa(**dados_pessoa)
#     print(p1.nome)



# implementação do professor
import json

from aula127a import CAMINHO_ARQUIVO, Pessoa, fazer_dump

# fazer_dump()

with open(CAMINHO_ARQUIVO, 'r', encoding='utf8') as arquivo:
    pessoas = json.load(arquivo)
    p1 = Pessoa(**pessoas[0])
    p2 = Pessoa(**pessoas[1])
    p3 = Pessoa(**pessoas[2])

    print(p1.nome, p1.idade)
    print(p2.nome, p2.idade)
    print(p3.nome, p3.idade)