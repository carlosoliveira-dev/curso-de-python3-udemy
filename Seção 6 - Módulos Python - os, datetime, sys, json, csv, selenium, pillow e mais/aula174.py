'''
os + shutil - Apagando, copiando, movendo e renomeando pastas com Python
Vamos copiar arquivos de uma pasta para outra.
Copiar -> shutil.copy
Copiar Árvore recursivamente -> shutil.copytree
Apagar Árvore recursivamente -> shutil.rmtree
Apagar arquivos -> os.unlink
Renomear/Mover -> shutil.move ou os.rename
'''
import os
import shutil

HOME = os.path.expanduser('~')
DESKTOP = os.path.join(HOME, 'OneDrive', 'Desktop')
PASTA_IMAGENS = os.path.join('/Users', 'trade', 'OneDrive', 'Pictures')
NOVA_PASTA = os.path.join(DESKTOP, 'Imagens')
PASTA_RENOMEADA = NOVA_PASTA + '_EITA'

input('precione enter para copiar a pasta "Pictures":')

shutil.copytree(
    PASTA_IMAGENS,
    NOVA_PASTA,
    ignore=shutil.ignore_patterns('desktop.ini')
)

input('precione enter para renomear a pasta "Imagens":')

shutil.move(NOVA_PASTA, PASTA_RENOMEADA)

print('Apague a pasta manualmente!')
