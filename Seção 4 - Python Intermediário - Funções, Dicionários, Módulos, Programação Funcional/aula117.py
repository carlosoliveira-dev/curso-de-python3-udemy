'''
Tipos de dados do JSON:

String -> "Carlos"
Descrição: Texto entre aspas duplas.

Number -> 10, 3.14, -5
Descrição: Números inteiros ou decimais.

Boolean -> true, false
Descrição: Valores lógicos.

Null -> null
Descrição: Representa ausência de valor.

Object -> {"nome": "Carlos", "idade": 30}
Descrição: Coleção de pares chave-valor.

Array -> ["Python", "JavaScript", "Go"]
Descrição: Lista ordenada de valores.

'''
import json

pessoa = {
    'nome': 'Luiz Otávio 2',
    'sobrenome': 'Miranda',
    'enderecos': [
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R2', 'numero': 55},
    ],
    'altura': 1.8,
    'numeros_preferidos': (2, 4, 6, 8, 10),
    'dev': True,
    'nada': None,
}

with open('aula117.json', 'w', encoding='utf8') as arquivo:
    json.dump(
        pessoa,
        arquivo,
        ensure_ascii=False,
        indent=2,
    )

with open('aula117.json', 'r', encoding='utf8') as arquivo:
    pessoa = json.load(arquivo)
    print(pessoa)
    print(type(pessoa))
    print(pessoa['nome'])