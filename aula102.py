# Variáveis livres + nonlocal (locals, globals)

# print('globals')
# print(*globals().items(), sep='\n')

# print('locals')
# print(*locals().items(), sep='\n')

# def fora(x):
#     a = x # é uma variável livre porque não está definida na função interna

#     def dentro():
#         print(dentro.__code__.co_freevars) # a é uma variável livre dentro dessa função
#         return a
#     return dentro


# dentro1 = fora(10)
# dentro2 = fora(20)

# print(f'{dentro1()=}')
# print(f'{dentro2()=}')



def concatenar(string_inicial):
    valor_final = string_inicial

    def interna(valor_a_concatenar=''):
        nonlocal valor_final
        '''
          nonlocal = 'essa variável não é local, procure no escopo acima'
          sem usar nonlocal, ao tentar concatenar a string
          teríamos um erro porque essa variável é uma variável livre
          e o python só permite ler essa variável
        '''
        valor_final += valor_a_concatenar
        return valor_final
    return interna


c = concatenar('a')
print(c('b'))
print(c('c'))
print(c('d'))
final = c()
print(f'{final=}')