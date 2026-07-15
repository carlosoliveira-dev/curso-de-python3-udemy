# software para acessar qualquer banco de dados
# docker compose up -d
# pip install pymysql
# pip install types-pymysql
# pip install python-dotenv
# https://dbeaver.io/
# PyMySQL - um cliente MySQL feito em Python Puro
# Doc: https://pymysql.readthedocs.io/en/latest/
# Pypy: https://pypi.org/project/pymysql/
# GitHub: https://github.com/PyMySQL/PyMySQL
import pymysql

connection = pymysql.connect(
    host='localhost',
    user='usuario',
    password='senha',
    database='base_de_dados',
)

with connection:
    with connection.cursor() as cursor:
        # CONSULTAS SQL
        print(cursor)
