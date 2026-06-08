# isinstace - para saber se objeto é de determinado tipo
lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2),
    {0, 1}, {'nome': 'Luiz'},
]

for item in lista:
    if isinstance(item, set):
        print('SET')
        item.add(5)
        print(item, isinstance(item, set))
        print()

    elif isinstance(item, tuple):
        print('TUPLE')
        print(item)
        print()

    elif isinstance(item, list):
        print('LIST')
        print(item)
        print()

    elif isinstance(item, dict):
        print('DICT')
        print(item)
        print()

    elif isinstance(item, str):
        print('STR')
        print(item.upper())
        print()

    elif isinstance(item, bool):
        print('BOOL')
        print(item)
        print()
    
    elif isinstance(item, (int, float)): # int ou float
        print('INT OR FLOAT')
        print(item, item * 2)
        print()

    else:
        print('OTHER TYPE')
        print(item)
        print()
