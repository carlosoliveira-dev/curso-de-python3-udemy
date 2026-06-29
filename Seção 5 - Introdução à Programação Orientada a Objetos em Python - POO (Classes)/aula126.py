# __dict__ e vars para atributos de instância
class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade


dados = {'nome': 'João', 'idade': 35}
p1 = Pessoa(**dados) 
# p1 = Pessoa(nome='João', idade=35) # assim que o python interpreta o desempacotamento do dict

# p1.nome = 'EITA' # modifica o atributo
# print(p1.idade)
# del p1.idade # apaga um atributo

p1.__dict__['outra'] = 'coisa' # cria um atributo usando o dict
p1.__dict__['nome'] = 'EITA'
# del p1.__dict__['nome'] # apaga o atributo usando o dict

#  imprime o dict do objeto
print(p1.__dict__)
print(vars(p1))

print(p1.outra)
print(p1.nome)

# print(vars(p1))
# print(p1.nome)