'''
os + shutil - Copiando arquivos com Python
Vamos copiar arquivos de uma pasta para outra.
Copiar -> shutil.copy
'''
import os
import shutil

HOME = os.path.expanduser('~')
DESKTOP = os.path.join(HOME, 'OneDrive', 'Desktop')
PASTA_ORIGINAL = os.path.join(DESKTOP, 'PASTA_ORIGINAL')
NOVA_PASTA = os.path.join(DESKTOP, 'NOVA_PASTA')
CAMINHO_ARQUIVO = os.path.join(PASTA_ORIGINAL, 'arquivo.txt')

print('HOME:', HOME)
print('DESKTOP:', DESKTOP)
print('PASTA_ORIGINAL:', PASTA_ORIGINAL)
print('NOVA_PASTA:', NOVA_PASTA)
print('CAMINHO_ARQUIVO:', CAMINHO_ARQUIVO)
print()

os.makedirs(PASTA_ORIGINAL, exist_ok=True)
os.makedirs(NOVA_PASTA, exist_ok=True)

with open(CAMINHO_ARQUIVO, 'w', encoding='utf8') as arquivo:
    arquivo.write('hello world!')

input('Precione enter para copiar o arquivo para a pasta "NOVA_PASTA":')

for root, dirs, files in os.walk(PASTA_ORIGINAL):
    for dir_ in dirs:
        caminho_novo_diretorio = os.path.join(
            root.replace(PASTA_ORIGINAL, NOVA_PASTA), dir_
        )

    for file in files:
        caminho_arquivo = os.path.join(root, file)

        novo_caminho_arquivo = os.path.join(
            root.replace(PASTA_ORIGINAL, NOVA_PASTA), file
        )

        shutil.copy(caminho_arquivo, novo_caminho_arquivo)

print('Cópia concluída com sucesso...')
