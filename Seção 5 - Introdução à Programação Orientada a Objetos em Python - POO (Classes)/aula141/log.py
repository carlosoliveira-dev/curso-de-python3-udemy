# Abstração
# Herança - é um
from pathlib import Path

# / concatena usando a barra do sistema operacional
LOG_FILE = Path(__file__).parent / 'log.txt'


class Log:
    def _log(self, msg):
        raise NotImplementedError('Implemente o método log')

    def log_error(self, msg):
        return self._log(f'Error: {msg}')

    def log_success(self, msg):
        return self._log(f'Success: {msg}')


class LogFileMixin(Log):
    # a assinatura do método deve ser a mesma em todas as subclasses
    # não pode mudar o tipo do(s) parâmetro(s) nem o retorno do método
    def _log(self, msg):
        msg_fomatada = f'{msg} ({self.__class__.__name__})'
        print('Salvando no log:', msg_fomatada)
        with open(LOG_FILE, 'a', encoding='utf8') as arquivo:
            arquivo.write(msg_fomatada)
            arquivo.write('\n')


class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')


# se o __name__ do módulo for '__main__'
# significa que estou executando ele diretamente
# ao invés de importando em outro 
if __name__ == '__main__':
    lp = LogPrintMixin()
    lp.log_error('qualquer coisa')
    lp.log_success('Que legal')
    lf = LogFileMixin()
    lf.log_error('qualquer coisa')
    lf.log_success('Que legal')