import string as s
from secrets import SystemRandom as Sr

print('Tabelas de caracteres:')
print(s.ascii_letters)
print(s.digits)
print(s.punctuation)
print()

print('senha gerada randomicamente:')
print(''.join(Sr().choices(s.ascii_letters + s.digits + s.punctuation, k=64)))
