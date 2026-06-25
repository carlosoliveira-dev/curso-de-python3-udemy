'''
    Funções decoradoras e decoradores com classes
    Essas funções recebem a classe como primeiro argumento
    e a gente pode fazer o que quiser com ela
    desde que retorne a própria classe no final da função
    A função meu_repr recebe self como primeiro argumento se comportando
    como se fosse um método, perceba que a função não é executada na hora
    e fica no lugar do método __repr__ da classe original
'''
def meu_repr(self):
    class_name = self.__class__.__name__
    class_dict = self.__dict__
    class_repr = f'{class_name}({class_dict})'
    return class_repr


def adiciona_repr(cls):
    ''' Passa a referência da função '''
    cls.__repr__ = meu_repr
    return cls


@adiciona_repr
class Time:
    def __init__(self, nome):
        self.nome = nome


@adiciona_repr
class Planeta:
    def __init__(self, nome):
        self.nome = nome


brasil = Time('Brasil')
portugal = Time('Portugal')

terra = Planeta('Terra')
marte = Planeta('Marte')

print(brasil)
print(portugal)

print(terra)
print(marte)
