'''
argparse.ArgumentParser para argumentos mais complexos
Tutorial Oficial:
https://docs.python.org/pt-br/3/howto/argparse.html
python aula188.py -b "exemplo de argumento"
python aula188.py --help
python aula188.py -v
'''
from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument(
    '-b', '--basic',
    help='Mostra "Olá mundo" na tela',
    # type=str, # Tipo do argumento
    metavar='STRING',
    # default='Olá mundo', # Valor padrão
    required=False,
    action='append',  # Recebe o argumento mais de uma vez
    # nargs='+', # Recebe mais de um valor e transforma em uma lista
)
parser.add_argument(
    '-v', '--verbose',
    help='Mostra logs',
    action='store_true'
)
args = parser.parse_args()

if args.basic is None:
    print('Você não passou o valor de b.')
    print(args.basic)
else:
    print('O valor de basic:', args.basic)

''' comando para setar como true: -v '''
print(args.verbose)
