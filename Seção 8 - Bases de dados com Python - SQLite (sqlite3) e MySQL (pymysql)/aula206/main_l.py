# PyMySQL - um cliente MySQL feito em Python Puro
# Doc: https://pymysql.readthedocs.io/en/latest/
# Pypy: https://pypi.org/project/pymysql/
# GitHub: https://github.com/PyMySQL/PyMySQL
import os
from typing import cast

import dotenv
import pymysql
import pymysql.cursors

TABLE_NAME = 'customers'
CURRENT_CURSOR = pymysql.cursors.SSDictCursor

dotenv.load_dotenv()

connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
    charset='utf8mb4',
    cursorclass=CURRENT_CURSOR,
)

with connection:
    with connection.cursor() as cursor:
        cursor.execute(  # type: ignore
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
            'id INT NOT NULL AUTO_INCREMENT, '
            'nome VARCHAR(50) NOT NULL, '
            'idade INT NOT NULL, '
            'PRIMARY KEY (id)'
            ') '
        )
        # CUIDADO: ISSO LIMPA A TABELA
        cursor.execute(f'TRUNCATE TABLE {TABLE_NAME}')  # type: ignore

    connection.commit()

    # Inserindo vários valores usando placeholder e um tupla de tuplas
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) '
            'VALUES '
            '(%s, %s) '
        )
        data4 = (
            ("Siri", 22, ),
            ("Helena", 15, ),
            ("Luiz", 18, ),
        )
        result = cursor.executemany(sql, data4)  # type: ignore

    connection.commit()

    # Editando com UPDATE, WHERE e placeholders no PyMySQL
    with connection.cursor() as cursor:
        # garante que cursor é do tipo definido em CURRENT_CURSOR
        cursor = cast(CURRENT_CURSOR, cursor)

        sql = (
            f'UPDATE {TABLE_NAME} '
            'SET nome=%s, idade=%s '
            'WHERE id=%s'
        )
        cursor.execute(sql, ('Eleonor', 102, 3))
        cursor.execute(f'SELECT * FROM {TABLE_NAME} ')

        print('For 1: ')
        ''' usar com um grande volume de dados '''
        for row in cursor.fetchall_unbuffered():
            print(row)

            if row['id'] >= 1:
                break

        print()

        ''' cursor continua de onde parou '''
        print('For 2: ')
        for row in cursor.fetchall_unbuffered():
            print(row)

    connection.commit()
