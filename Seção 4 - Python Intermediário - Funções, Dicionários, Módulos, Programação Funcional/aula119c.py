# Exercício - salvar a lista de tarefas em arquivo json
# minha implementação
import os
import json

def listar(tarefas):
    print()
    if not tarefas:
        print('Nenhuma tarefa para listar')
        return

    print('Tarefas:')
    for tarefa in tarefas:
        print(f'\t{tarefa}')
    print()


def desfazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('Nenhuma tarefa para desfazer')
        return

    tarefa = tarefas.pop()
    print(f'{tarefa=} removida da lista de tarefas.')
    tarefas_refazer.append(tarefa)
    salvar_tarefas_json(tarefas, 'aula119c_tarefas.json')
    salvar_tarefas_json(tarefas_refazer, 'aula119c_tarefas_refazer.json')
    print()
    listar(tarefas)


def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer:
        print('Nenhuma tarefa para refazer')
        return

    tarefa = tarefas_refazer.pop()
    print(f'{tarefa=} adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    salvar_tarefas_json(tarefas, 'aula119c_tarefas.json')
    salvar_tarefas_json(tarefas_refazer, 'aula119c_tarefas_refazer.json')
    print()
    listar(tarefas)


def salvar_tarefas_json(tarefas, nome_arquivo):
    with open(nome_arquivo, 'w', encoding='utf8') as arquivo:
            json.dump(
                tarefas,
                arquivo,
                ensure_ascii=False,
                indent=2,
            )


def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('Você não digitou uma tarefa.')
        return
    print(f'{tarefa=} adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    salvar_tarefas_json(tarefas, 'aula119c_tarefas.json')
    print()
    listar(tarefas)


tarefas = []
tarefas_refazer = []

while True:

    
    with open('aula119c_tarefas.json', 'r', encoding='utf8') as arquivo:
        tarefas = json.load(arquivo)

    with open('aula119c_tarefas_refazer.json', 'r', encoding='utf8') as arquivo:
        tarefas_refazer = json.load(arquivo)

    print('Comandos: listar, desfazer e refazer')
    tarefa = input('Digite uma tarefa ou comando: ')

    comandos = {
        'listar': lambda: listar(tarefas),
        'desfazer': lambda: desfazer(tarefas, tarefas_refazer),
        'refazer': lambda: refazer(tarefas, tarefas_refazer),
        'clear': lambda: os.system('clear'),
        'adicionar': lambda: adicionar(tarefa, tarefas),
    }
    comando = comandos.get(tarefa) if comandos.get(tarefa) is not None else \
        comandos['adicionar']
    comando()
