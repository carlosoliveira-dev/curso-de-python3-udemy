################################################################################
#
# Uso de `global` e `nonlocal` para mudar o comportamento
#
# Quando você define um nome em determinado escopo, o Python assume que aquele
# nome é único naquele escopo. Por isso, é impossível modificar o valor de um
# nome do escopo externo sem informar isso ao interpretador.
#
# ** `global` - Para modificar nomes do escopo global dentro de qualquer escopo
#               local, precisamos usar a palavra chave `global`.
# ** `nonlocal` -  Para modificar os nomes do escopo `enclosing` dentro de qualquer
#               escopo local, precisamos usar a palavra chave `nonlocal`.
#
################################################################################


"""
ALTERAR UMA VARIÁVEL FORA DO SEU ESCOPO É UMA MÁ PRÁTICA DE PROGRAMAÇÃO
"""

nome_global = "nome_global"


def func_global() -> None:
    global nome_global # ao invés de criar outra variável use a variável declarada acima

    nome_enclosing = "nome_enclosing"
    nome_global = 123456

    def func_interna() -> None:
        def func3() -> None:
            def func4() -> None:
                nonlocal nome_enclosing # encontre a variável em uma das funções

                nome_local = "nome_local"
                nome_enclosing = 654321

                print("func_interna", nome_enclosing)

            func4()

        func3()

    func_interna()
    print("func_global", nome_enclosing)


func_global()
# print("NO GLOBAL", nome_global)
