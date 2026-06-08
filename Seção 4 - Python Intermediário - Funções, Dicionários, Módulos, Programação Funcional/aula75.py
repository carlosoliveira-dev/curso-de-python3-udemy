# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicador = criar_multiplicador(2)
triplicador = criar_multiplicador(3)
quadriplicador = criar_multiplicador(4)

print(f'{duplicador(10)=}\n')
print(f'{triplicador(10)=}\n')
print(f'{quadriplicador(10)=}')
