'''
  Ambientes virtuais em Python (venv)
  Um ambiente virtual carrega toda a sua instalação
  do Python para uma pasta no caminho escolhido.
  Ao ativar um ambiente virtual, a instalação do
  ambiente virtual será usada.
  venv é o módulo que vamos usar para
  criar ambientes virtuais.
  Você pode dar o nome que preferir para um
  ambiente virtual, mas os mais comuns são:
  venv env .venv .env
  
  Como criar ambientes virtuais
  Abra a pasta do seu projeto no terminal
  e digite:
  python -m venv venv
  
  Ativando e desativando meu ambiente virtual
  Windows: .\venv\Scripts\activate
  Linux e Mac ou windows com git bash: source venv/Scripts/activate
  Desativar: deactivate

  mostra a versão do pip e o path do ambiente virtual
  pip --version

  instalar pacotes
  pip install pymysql

  instalar versão específica
  pip install pymysql==0.10.0
  
  atualizar pacote para última versão
  pip install pymysql --upgrade

  desinstalar pacotes
  pip uninstall pymysql

  listar os pacotes instalados
  pip freeze
  
  Criando e usando um requirements.txt
  pip freeze > requirements.txt

  
  Instalando tudo do requirements.txt
  Crie e ative um ambiente virtual para não instalar pacotes no python global
  pip install -r requirements.txt

  listar as versões disponíveis do pacote e a versão instalada
  pip index versions pymysql

  

  '''

