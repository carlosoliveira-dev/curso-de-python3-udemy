# try e except para tratar exceções
# a = 18
# b = 0
# c = a / b

try:
    a = 18
    b = 0
    # print(b[0])
    # print('Linha 1'[1000])
    c = a / b
    print('SE DER EXCEÇÃO NEM EXECUTA ESSA LINHA')
except ZeroDivisionError:
    print('Dividiu por zero.')
except NameError:
    print('Nome b não está definido')
except TypeError:
    print('TypeError')
except IndexError:
    print('IndexError')
except Exception:
    print('ERRO DESCONHECIDO.')

print('FIM DO SCRIPT')
