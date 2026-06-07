# dir, hasattr e getattr em Python
string = 'Luiz'
metodo = 'upper'

if hasattr(string, metodo): # verifica se o objeto tem o método
    print('Existe upper')
    print(getattr(string, metodo)()) # executa o método dinamicamente
else:
    print('Não existe o método', metodo)

'''
comandos no debug console
    dir(string) # mostra uma lista de todos os métodos do objeto
'''