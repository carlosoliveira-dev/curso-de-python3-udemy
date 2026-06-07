# count é um iterador sem fim (itertools)
from itertools import count

c1 = count(step=8, start=8)
r1 = range(8, 100, 8)

print(f'{hasattr(c1, '__iter__')=}') # é um iterável
print(f'{hasattr(c1, '__next__')=}') # é um iterator
print(f'{hasattr(r1, '__iter__')=}') # é um iterável
print(f'{hasattr(r1, '__next__')=}') # não é um iterator por não conter o método next

print('count')
for i in c1:
    if i >= 100:
        break
    print(i)
print()

# print('range')
# for i in r1:
#     print(i)
