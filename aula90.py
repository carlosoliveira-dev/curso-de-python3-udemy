import sys

# Generator expression, Iterables e Iterators em Python
iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable)  # tem __iter__ e __next__

# a lista já está pronta e salva inteira na memória
lista = [n for n in range(1000000)]

# generator é uma função que pausa depois da primeira execução
# cada vez que a gente precisar do próximo valor desse generator
# ele vai processar e entregar o próximo
# não fica salvo na memória ocupando espaço
# não tem tamanho usando len(generator)
# não dá pra acessar os elementos por índice igual listas
generator = (n for n in range(1000000))

print('tamanho da lista:', sys.getsizeof(lista))
print('tamanho do generator:', sys.getsizeof(generator))

print(generator)

print('primeiro valor do generator:', next(generator))
print('segundo valor do generator:', next(generator))
print('terceiro valor do generator:', next(generator))

# for n in generator:
#     print(n)
