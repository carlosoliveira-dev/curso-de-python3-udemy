"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
"""

x = 1

def escopo():
    global x # permite que o x do escopo global possa ser modificado aqui
    x = 10
    print(f'dentro de escopo() {x=}')
    def outra_funcao():
        global x # permite modificar a variável do escopo maior
        x = 11
        y = 2
        print(f'dentro de outra_funcao() {x=}, {y=}')

    outra_funcao()
    print(f'dentro de escopo() {x=}')


print(f'fora das funções {x=}')
print('chamando escopo()')
escopo()
print(f'depois de chamar escopo() {x=}')