def executa(funcao, *args):
    return funcao(*args)


def soma(x, y):
    return x + y


def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica


# duplica = cria_multiplicador(2)
duplica = executa( # tenta executar a primeira função lambda, por isso temos que passar o parâmetro m
    # recebe m : retorna outra lambda que recebe n : lambda interna retorna n * m
    lambda m: lambda n: n * m, # faz a mesma coisa que a função cria_multiplicador
    2 # o parâmetro m recebe esse valor
)
print('função lambda que duplica valores:', duplica(6))

# print('soma com lambda:', (lambda x, y: x + y)(2, 3)) # parênteses servem para executar e passar argumentos
# print('soma com função chamando a lambda:', executa(lambda x, y: x + y, 2, 3 ))
# print('soma com função normal:', soma(2, 3))

print(
    'recebe argumentos posicionais e retorna a soma deles:',
    executa(
        lambda *args: sum(args),
        1, 2, 3, 4, 5, 6, 7
    )
)