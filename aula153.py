'''
    Método especial __call__
    callable é algo que pode ser executado com parênteses
    Em classes normais, __call__ faz a instância de uma
    classe ser "callable"
'''
class CallMe:
    def __init__(self, phone):
        self.phone = phone

    def __call__(self, nome):
        print(nome, 'está chamando', self.phone)
        return 'RESPOSTA'


call1 = CallMe('(23)94587-6545')
retorno = call1('Luiz Otávio')
print(retorno)
