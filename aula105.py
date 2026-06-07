# Decoradores com parâmetros
def fabrica_de_decoradores(a=None, b=None, c=None):
    def fabrica_de_funcoes(func): # função decoradora
        print(f'Decoradora {a, b, c}')

        def aninhada(*args, **kwargs):
            print('Parâmetros do decorador, ', a, b, c)
            print('Aninhada')
            res = func(*args, **kwargs)
            return res
        return aninhada
    
    return fabrica_de_funcoes


@fabrica_de_decoradores(1, 2, 3) # mais uma camada de abstração antes do python executar a função decoradora
def soma(x, y):
    return x + y


decoradora = fabrica_de_decoradores(50, 77, 29)
multiplica = decoradora(lambda x, y: x * y)

multiplica2 = fabrica_de_decoradores(77, 77, 77)(lambda x, y: x * y) # da pra chamar assim uma função que retorna outra

dez_mais_cinco = soma(10, 5)
dez_vezes_cinco = multiplica(10, 5)
quinze_vezes_dois = multiplica2(15, 2)
print(quinze_vezes_dois)
print(dez_mais_cinco)
print(dez_vezes_cinco)