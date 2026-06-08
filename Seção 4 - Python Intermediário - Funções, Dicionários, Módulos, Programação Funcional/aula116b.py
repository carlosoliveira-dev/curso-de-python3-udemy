# Leia também: https://www.otaviomiranda.com.br/2020/normalizacao-unicode-em-python/
caminho_arquivo = 'aula116.txt'

'''
  Modos de abertura de um arquivo:
  r (leitura), w (escrita), x (para criação)
  a (escreve ao final), b (binário)
  t (modo texto), + (leitura e escrita)

  usar 'w' habilita só a escrita no arquivo
  então o arquivo será apagado e regravado a cada
  execução do script

  usando 'a' o arquivo não é apagado e começa a gravar
  no final dele

  encoding='utf8'(codificação de caracteres) é importante porque
  no windows alguns caracteres como o 'ç' não aparecem corretamente
'''
with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
    arquivo.write('Atenção\n')
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.writelines(
        ('Linha 3\n', 'Linha 4\n')
    )
