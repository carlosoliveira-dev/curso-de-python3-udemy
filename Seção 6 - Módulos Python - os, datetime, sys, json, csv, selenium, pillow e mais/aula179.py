'''
csv.reader e csv.DictReader
csv.reader lê o CSV em formato de lista
csv.DictReader lê o CSV em formato de dicionário
'''
import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / 'aula179.csv'

with open(CAMINHO_CSV, 'r', encoding='utf8') as arquivo:
    leitor_ = csv.DictReader(arquivo)

    for linha_ in leitor_:
        print(linha_['Nome'], linha_['Idade'], linha_['Endereço'])

with open(CAMINHO_CSV, 'r', encoding='utf8') as arquivo:
    leitor = csv.reader(arquivo)

    for linha in leitor:
        print(linha)
