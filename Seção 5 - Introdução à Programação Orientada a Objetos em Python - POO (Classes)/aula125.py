# Atributos de classe
class Pessoa:
    # declarando um atributo de classe
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        # acessando um atributo de classe
        return Pessoa.ano_atual - self.idade


p1 = Pessoa('João', 35)
p2 = Pessoa('Helena', 12)

print(Pessoa.ano_atual)
# o cálculo fica errado para todas as instâncias da classe
Pessoa.ano_atual = 1

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())