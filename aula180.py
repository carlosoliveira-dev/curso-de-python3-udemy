'''
csv.writer e csv.DictWriter para escrever em CSV
csv.reader lê o CSV em formato de lista
csv.DictReader lê o CSV em formato de dicionário
'''
import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / 'aula180.csv'

lista_clientes = [
    {'Nome': 'Luiz Otávio', 'Endereço': 'Av 1, 22'},
    {'Nome': 'João Silva', 'Endereço': 'R. 2, "1"'},
    {'Nome': 'Maria Sol', 'Endereço': 'Av B, 3A'},
]

with open(CAMINHO_CSV, 'w', encoding='utf8') as arquivo:
    nome_colunas = lista_clientes[0].keys()
    escritor = csv.DictWriter(
        arquivo,
        fieldnames=nome_colunas
    )
    escritor.writeheader()

    for cliente in lista_clientes:
        print(cliente)
        escritor.writerow(cliente)

# usando listas
lista_clientes_ = [
    ['Luiz Otávio', 'Av 1, 22'],
    ['João Silva', 'R. 2, "1"'],
    ['Maria Sol', 'Av B, 3A'],
]
with open(CAMINHO_CSV, 'w', encoding='utf8') as arquivo:
    # nome_colunas = lista_clientes_[0].keys()
    nome_colunas_ = ['Nome', 'Endereço']
    escritor_ = csv.writer(arquivo)

    escritor_.writerow(nome_colunas_)

    for cliente_ in lista_clientes_:
        escritor_.writerow(cliente_)
