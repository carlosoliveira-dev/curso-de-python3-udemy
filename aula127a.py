# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.

# minha implementação
# import json


# class Pessoa:
#     def __init__(self, nome):
#         self.nome = nome

# p1 = Pessoa('Carlos Júnior Torres de Oliveira')

# # salva a instância em um arquivo no formato json
# with open('aula127.json', 'w', encoding='utf8') as arquivo:
#     json.dump(
#         p1.__dict__,
#         arquivo,
#         ensure_ascii=False,
#         indent=2,
#     )


# implementação do professor
import json

CAMINHO_ARQUIVO = 'aula127.json'


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


p1 = Pessoa('João', 33)
p2 = Pessoa('Helena', 21)
p3 = Pessoa('Joana', 11)
bd = [vars(p1), p2.__dict__, vars(p3)]


def fazer_dump():
    with open(CAMINHO_ARQUIVO, 'w', encoding='utf8') as arquivo:
        print('FAZENDO DUMP')
        json.dump(bd, arquivo, ensure_ascii=False, indent=2)

'''
  executa a função fazer_dump() somente se o módulo for executado diretamente
  caso esse módulo seja importado por outro é necessário chamar a função

  isso serve para executar só o código que queremos ao executar o módulo diretamente
'''
if __name__ == '__main__':
    print('ELE É O __main__')
    fazer_dump()