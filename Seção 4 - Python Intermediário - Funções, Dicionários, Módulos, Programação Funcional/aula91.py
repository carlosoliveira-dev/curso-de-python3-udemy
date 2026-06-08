# Introdução às Generator functions em Python
# generator = (n for n in range(1000000))

# # minha implementação
# def generator_function():
#     yield 'primeiro yield' # retorna e pausa
#     yield 'segundo yield'
#     yield 'último yield executado'
#     return 'FIM DA FUNÇÃO' # mensagem aparece na exceção

# gf = generator_function()

# print(next(gf))
# print(next(gf))
# print(next(gf))
# next(gf) # gera a exceção que mostra pro python que a função acabou

# for mensagem in gf:
#     print(mensagem)




# toda função que tem yield é uma Generator function
def generator(n=0, maximum=10):
    while True:
        yield n # pausar aqui e na próxima chamada vai para a linha de baixo
        n += 1

        if n >= maximum:
            return


gen = generator(maximum=10)
for n in gen:
    print(n)