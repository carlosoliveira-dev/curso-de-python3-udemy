"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
Não temos acesso a nomes de escopos internos nos escopos externos.
A palavra global faz uma variável do escopo externo ser a mesma no escopo interno.
Cada função tem o seu escopo.
O escopo da função proteje as variáveis de acessos externos criando uma camada de isolação local.
As variáveis de uma função são chamadas de variáveis locais.
"""

x = 1


def escopo():
    # global x # significa que essa variável x é o mesmo x declarado fora
    x = 10

    def outra_funcao():
        # global x
        x = 11 # se esse x for comentado o python vai procurar no escopo mais externo até encontrar.
        y = 2
        print(x, y)

    outra_funcao()
    print(x)


# print(x)
escopo()
# print(x)