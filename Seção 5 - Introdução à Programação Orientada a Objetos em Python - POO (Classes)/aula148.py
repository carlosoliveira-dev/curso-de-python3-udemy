'''
    __new__ e __init__ em classes Python
    __new__ é o método responsável por criar e
    retornar o novo objeto. Por isso, new recebe cls(recebe a classe).
    __new__ ❗️DEVE retornar o novo objeto❗️
    __init__ é o método responsável por inicializar
    a instância. Por isso, init recebe self.
    __init__ ❗️NÃO DEVE retornar nada (None)❗️
    __init__ é usado quando a gente precisa interceptar
    a criação de um objeto '''
class A:
    def __new__(cls, *args, **kwargs):
        print('Antes de criar a instância')
        instancia = super().__new__(cls)
        print('Depois de criar a instância')
        return instancia

    def __init__(self, x):
        self.x = x
        print('Sou o init da classe')

    def __repr__(self):
        return 'A()'


a = A(123)
print(a.x)
print()

'''
    O que o Python faz por debaixo dos panos:
    passa a classe para o __new__ que retorna a instância
    depois chama o __init__ para inicializar o objeto 
    object é a super classe de uma classe '''
b = object.__new__(A)
b.__init__(1111)
print(b.x)
