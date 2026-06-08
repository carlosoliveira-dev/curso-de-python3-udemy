'''
  Exercício - Lista de tarefas com desfazer e refazer
  Música para codar =)
  Everybody wants to rule the world - Tears for fears
  todo = [] -> lista de tarefas
  todo = ['fazer café'] -> Adicionar fazer café
  todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
  desfazer = ['fazer café',] -> Refazer ['caminhar']
  desfazer = [] -> Refazer ['caminhar', 'fazer café']
  refazer = todo ['fazer café']
  refazer = todo ['fazer café', 'caminhar']
'''
# minha implementação
import subprocess

tarefas = []
auxiliar = []

comandos = ['listar', 'desfazer', 'refazer', 'clear', 'sair']

while True:
    print('Comandos: ', *comandos)
    entrada = input('Digite uma tarefa ou comando: ')

    if entrada in comandos:
        if entrada == 'listar':
            if not tarefas:
                print('NENHUMA TAREFA CADASTRADA')
            else:
                print('TAREFAS:', *tarefas)
        elif entrada == 'desfazer':
            if tarefas:
                auxiliar.append(tarefas.pop())
            else:
                print('Nada a desfazer')
        elif entrada == 'refazer':
            if auxiliar:
                tarefas.append(auxiliar.pop())
            else:
                print('Nada a refazer')
        elif entrada == 'clear':
            subprocess.run('clear')
        elif entrada == 'sair':
            break
    else:
        tarefas.append(entrada)
    print()
