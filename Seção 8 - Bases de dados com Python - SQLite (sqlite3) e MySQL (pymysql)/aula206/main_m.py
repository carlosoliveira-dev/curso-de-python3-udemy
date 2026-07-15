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
CURRENT_CURSOR = pymysql.cursors.DictCursor

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
        cursor = cast(CURRENT_CURSOR, cursor)

        sql = (
            f'UPDATE {TABLE_NAME} '
            'SET nome=%s, idade=%s '
            'WHERE id=%s'
        )
        cursor.execute(sql, ('Eleonor', 102, 3))

        cursor.execute(
            f'SELECT id from {TABLE_NAME} ORDER BY id DESC LIMIT 1'
        )

        lastIdFromSelect = cursor.fetchone()

        resultFromSelect = cursor.execute(f'SELECT * FROM {TABLE_NAME} ')

        data6 = cursor.fetchall()

        for row in data6:
            print(row)

        print()
        print('resultFromSelect', resultFromSelect)
        print('len(data6)', len(data6))
        print('rowcount', cursor.rowcount)
        print('lastrowid', cursor.lastrowid)
        print('lastrowid na mão', lastIdFromSelect)

        cursor.scroll(0, 'absolute')
        print('rownumber', cursor.rownumber)

    connection.commit()
