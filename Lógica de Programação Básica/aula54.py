# minha solução do exercício
# lista_de_compras = []

# while True:
#     print('Selecione uma opção')
#     opcao = input('[i]nserir [a]pagar [l]istar [s]air: ')
#     if opcao.lower() == 'i':
#         novo_item = input('Escreva o que deseja adicionar na lista: ')
#         lista_de_compras.append(novo_item)
#         print('---')
#         print('Lista Completa: ', end='')
#         for i, item in enumerate(lista_de_compras):
#             print(i, item, end=', ')
#         else:
#             print('\n---')
#         continue
#     elif opcao.lower() == 'a':
#         indice_para_apagar = int(input("Escolha o índice para apagar: "))
#         del lista_de_compras[indice_para_apagar]
#         print('---')
#         print('Lista Completa: ', end='')
#         for i, item in enumerate(lista_de_compras):
#             print(item, end=', ')
#         else:
#             print('\n---')
#         continue
#     elif opcao.lower() == 'l':
#         if lista_de_compras:
#             print('Lista Completa: ', end='')
#             for i, item in enumerate(lista_de_compras):
#                 print(i, item, end=', ')
#             else:
#                 print('\n---')
#             print('---')
#         else:
#             print('Não há itens na lista')
#             print()
#     elif opcao.lower() == 's':
#         break
    
# solução do professor
"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
import subprocess

lista = []

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        subprocess.run('clear')
        valor = input('Valor: ')
        lista.append(valor)
    elif opcao == 'a':
        indice_str = input(
            'Escolha o índice para apagar: '
        )

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor digite número int.')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')
    elif opcao == 'l':
        subprocess.run('clear')

        if len(lista) == 0:
            print('Nada para listar')

        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        print('Por favor, escolha i, a ou l.')