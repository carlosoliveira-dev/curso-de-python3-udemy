# Problema dos parâmetros mutáveis em funções Python
# o ideal é não usar tipos mutáveis como valor padrão de parâmetros em funções 
# python vai reutilizar sempre o mesmo parâmetro lista=[]
# essa lista não vai mais começar vazia depois que adicionar um novo item
# se o parâmetro for mutável não coloca valor padrão
def adiciona_clientes(nome, lista=[]):
    lista.append(nome)
    return lista

cliente1 = adiciona_clientes('luiz')
adiciona_clientes('Joana', cliente1)
adiciona_clientes('Fernando', cliente1)
cliente1.append('Edu')

cliente2 = adiciona_clientes('Helena')
adiciona_clientes('Maria', cliente2)

cliente3 = adiciona_clientes('Moreira')
adiciona_clientes('Vivi', cliente3)

print('Python não cria uma nova lista nas próximas chamadas da função')
print(f'{cliente1=}')
print(f'{cliente2=}')
print(f'{cliente3=}')
print()


# implementação ideal
def adiciona_clientes(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista

cliente1 = adiciona_clientes('luiz')
adiciona_clientes('Joana', cliente1)
adiciona_clientes('Fernando', cliente1)
cliente1.append('Edu')

cliente2 = adiciona_clientes('Helena')
adiciona_clientes('Maria', cliente2)

cliente3 = adiciona_clientes('Moreira')
adiciona_clientes('Vivi', cliente3)

print('se não passar a lista a função devolve uma lista nova completamente vazia')
print(f'{cliente1=}')
print(f'{cliente2=}')
print(f'{cliente3=}')