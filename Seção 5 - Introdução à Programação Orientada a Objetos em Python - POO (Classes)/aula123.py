# Escopo da classe e de métodos da classe
class Animal:
    # atributos de classe
    nome = 'Alex'

    def __init__(self, nome):
        # atributos de instância
        self.nome = nome

        variavel = 'valor'
        print(variavel)

    def comendo(self, alimento):
        return f'{self.nome} está comando {alimento}'

    def executar(self, *args, **kwargs):
        return self.comendo(*args, **kwargs)

    def escopo_de_classe(self):
        # acessando atributo de classe
        return f'{Animal.nome}'

leao = Animal(nome='Leão')
print(leao.nome)
print(leao.executar('maçã'))
print(leao.escopo_de_classe())