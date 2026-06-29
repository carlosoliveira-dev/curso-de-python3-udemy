'''
    Lidando com exceções no Context Manager
'''
class MyOpen:
    def __init__(self, caminho_arquivo, modo):
        self.caminho_arquivo = caminho_arquivo
        self.modo = modo
        self._arquivo = None

    def __enter__(self):
        print('ABRINDO ARQUIVO')
        self._arquivo = open(self.caminho_arquivo, self.modo, encoding='utf8')
        return self._arquivo
    
    ''' Tem acesso a tudo da exceção e pode fazer o que quiser'''
    def __exit__(self, class_exception, exception_, traceback_):
        print('FECHANDO ARQUIVO')
        self._arquivo.close()
        
        ''' recriando a mesma exceção'''
        # raise class_exception(*exception_.args).with_traceback(traceback_)

        print(class_exception)
        print(exception_)
        print(traceback_)

        ''' indica para o python que já tratei a exceção
            e ele pode ignorar o erro '''
        exception_.add_note('Minha nota')
        # return True


with MyOpen('aula149.txt', 'w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n', 123)
    arquivo.write('Linha 3\n')
    print('WITH', arquivo)
