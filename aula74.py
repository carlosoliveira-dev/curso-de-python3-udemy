"""
Closure e funções que retornam outras funções
"""

# # exemplo de adiamento de execução de uma função
# def criar_saudacao(saudacao, nome):
#     def saudar():
#         return f'{saudacao}, {nome}!'
#     return saudar


# s1 = criar_saudacao('Bom dia', 'Luiz')
# s2 = criar_saudacao('Boa noite', 'Luiz')

# # quando chamamos a função s1() isso é chamado de Closure(fechamento do fluxo da função)
# print(f'{s1=}\nExecução de s1:', s1(), '\n')
# print(f'{s2=}\nExecução de s2:', s2(), '\n')


# outro exemplo
def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar


# depois de executar essa linha a função criar_saudação não foi resolvida
# e o argumento fica armazenado no escopo da função e a call stack irá esperar até executar a função saudar
falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Boa noite')

for nome in ['Maria', 'Joana', 'Luiz']:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome), '\n')
