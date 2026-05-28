a = 'A'
b = 'B'
c = 1.1
formato = 'formato: ' + 'a={} b={} c={:.2f}'.format(a, b, c)
formato2 = 'formato2: ' + 'c={2:.2f} a={0} b={1}'.format(a, b, c) # posso escolher a ordem dos argumentos usando os índices dentro das chaves {}. O índice começa em 0.
formato3 = 'formato3: ' + 'c={nome3:.2f} a={nome1} b={nome2}'.format(nome1=a, nome2=b, nome3=c) # posso usar parâmetros nomeados dentro das chaves {}.

print(formato)
print(formato2)
print(formato3)