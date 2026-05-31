# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

def criar_multiplicador(multiplicando):
    def multiplicar(numero):
        return numero * multiplicando
    return multiplicar

duplicador = criar_multiplicador(2)
triplicador = criar_multiplicador(3)
quadriplicador = criar_multiplicador(4)

print(f'{duplicador(10)=}')
print(f'{triplicador(10)=}')
print(f'{quadriplicador(10)=}')
