'''
datetime.timedelta e dateutil.relativetimedelta (calculando datas)
Docs:
https://dateutil.readthedocs.io/en/stable/relativedelta.html
https://docs.python.org/3/library/datetime.html#timedelta-objects

pip install python-dateutil types-python-dateutil
'''
from datetime import datetime, timedelta

from dateutil.relativedelta import relativedelta


fmt = '%d/%m/%Y %H:%M:%S'

data_inicio = datetime.strptime('20/04/1987 09:30:30', fmt)
data_fim = datetime.strptime('12/12/2022 08:20:20', fmt)

delta = data_fim - data_inicio

print('diferença entre datas:', delta.days, delta.seconds, delta.microseconds)
print(delta.total_seconds())

# fazendo operações com datas
delta = timedelta(days=10, hours=2)
print('data_fim - delta:', data_fim - delta)
print('data_fim:', data_fim)
print('data_fim + 10m e 60s', data_fim + relativedelta(seconds=60, minutes=10))

print()
delta2 = relativedelta(data_fim, data_inicio)
print(delta2)
print('diferença em anos:', delta2.years)
print('diferença em dias:', delta2.days)
print()

print('data_inicio:', data_inicio)
print('data_fim:', data_fim)
print(data_fim > data_inicio)
print(data_fim < data_inicio)
print(data_fim == data_inicio)
