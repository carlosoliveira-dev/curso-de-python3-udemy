'''
Variáveis de ambiente com Python
Para variáveis de ambiente
Windows PS: $env:VARIAVEL="VALOR" | dir env:
Linux e Mac: export NOME_VARIAVEL="VALOR" | echo $VARIAVEL
Para obter o valor das variáveis de ambiente
os.getenv ou os.environ['VARIAVEL']
Para configurar variáveis de ambiente
os.environ['VARIAVEL'] = 'valor'
Ou usando python-dotenv e o arquivo .env
pip install python-dotenv
from dotenv import load_dotenv
load_dotenv()
https://pypi.org/project/python-dotenv/
OBS.: sempre lembre-se de criar um .env-example
esse arquivo serve para mostrar quais configurações o app
precisa pra funcionar
Nunca mande o arquivo .env para o repositório porque ele contém
senhas de acesso que devem ser protegidas
'''
import os

from dotenv import load_dotenv  # type: ignore

load_dotenv()

''' lista todas as variáveis de ambiente do sistema'''
# print(os.environ)

print(os.getenv('BD_PASSWORD'))
