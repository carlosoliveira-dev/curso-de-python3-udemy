from abc import ABC, abstractmethod


class Pessoa(ABC):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade):
        self._idade = idade


class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def adicionar_conta(self, conta: Conta):
        self.conta = conta


class Conta(ABC):
    def __init__(self, agencia, numero_conta, saldo):
        self._agencia = agencia
        self._numero_conta = numero_conta
        self._saldo = saldo

    @property
    def agencia(self):
        return self._agencia

    @property
    def numero_conta(self):
        return self._numero_conta

    @property
    def saldo(self):
        return self._saldo

    def depositar(self, valor):
        self._saldo += valor

    @abstractmethod
    def sacar(self, valor): ...


class ContaCorrente(Conta):
    def __init__(self, agencia, numero_conta, saldo):
        super().__init__(agencia, numero_conta, saldo)
        self.__limite = -100

    def sacar(self, valor):
        novo_saldo = self._saldo - valor
        if novo_saldo >= self.__limite:
            self._saldo = novo_saldo
            return novo_saldo
        raise ValueError('Limite da Conta Corrente atingido.')


class ContaPoupanca(Conta):
    def __init__(self, agencia, numero_conta, saldo):
        super().__init__(agencia, numero_conta, saldo)

    def sacar(self, valor):
        novo_saldo = self._saldo - valor
        if novo_saldo > 0:
            self._saldo = novo_saldo
            return novo_saldo
        raise ValueError('Conta Poupança não pode ter saldo negativo.')


class Banco:
    def __init__(self, id):
        self.id = id
        self.agencias = ['0001', '0002', '0003']
        self.clientes = []
        self.contas = []

    def adicionar_cliente(self, cliente: Cliente):
        self.clientes.append(cliente)

    def adicionar_conta(self, conta: Conta):
        self.contas.append(conta)

    def listar_clientes(self):
        print('lista de clientes:')
        for c in self.clientes:
            # imprimir todas as informações de cada cliente
            nome = c.nome
            idade = c.idade
            agencia = c.conta.agencia
            conta = c.conta.numero_conta
            saldo = c.conta.saldo

            dados = f'Nome: {nome}, Idade: {idade}'
            dados += f', Agência: {agencia}, Conta: {conta}, Saldo: {saldo}'

            print(dados)
        print()

    def __verifica_agencia(self, agencia) -> bool:
        # Checar se a agência é daquele banco
        if agencia in self.agencias:
            return True
        else:
            print('agência não está cadastrada no banco')
            return False

    def __verifica_cliente(self, cliente) -> bool:
        # Checar se o cliente é daquele banco
        if cliente in self.clientes:
            return True
        else:
            print('cliente não está cadastrado')
            return False

    def __verifica_conta(self, conta) -> bool:
        # Checar se a conta é daquele banco
        if conta in self.contas:
            return True
        else:
            print('conta não está cadastrada')
            return False

    def __autenticar(self, agencia, cliente, conta) -> bool:
        r = self.__verifica_agencia(agencia) and \
            self.__verifica_cliente(cliente)
        r = r and self.__verifica_conta(conta)
        return r

    def sacar(self, agencia, cliente, conta, valor):
        if not self.__autenticar(agencia, cliente, conta):
            print('usuário não autorizado')
            return
        print(f'sacando {valor} reais de {cliente.nome}')
        conta.sacar(valor)
        print(f'Novo saldo de {cliente.nome}: {conta.saldo}')


if __name__ == '__main__':
    bradesco = Banco('077')
    caixa = Banco('0478')

    conta_corrente_junior = ContaCorrente('0001', '32888', 0)
    conta_poupanca_junior = ContaPoupanca('0001', '32888', 500)
    conta_corrente_cassiano = ContaCorrente('0005', '575523', 450)

    junior = Cliente('Júnior', 28)
    junior.adicionar_conta(conta_corrente_junior)

    cassiano = Cliente('Cassiano', 21)
    cassiano.adicionar_conta(conta_corrente_cassiano)

    bradesco.adicionar_cliente(junior)
    bradesco.adicionar_conta(conta_corrente_junior)

    bradesco.adicionar_cliente(cassiano)
    bradesco.adicionar_conta(conta_corrente_cassiano)

    caixa.adicionar_cliente(junior)
    caixa.adicionar_conta(conta_poupanca_junior)
    caixa.adicionar_conta(conta_corrente_junior)

    caixa.listar_clientes()
    caixa.sacar(junior.conta.agencia, junior, conta_poupanca_junior, 100)
