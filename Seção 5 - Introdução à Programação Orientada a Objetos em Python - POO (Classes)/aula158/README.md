"""
CHECKLIST

[x]criar estrutura de classes
[x]Conta (ABC)
    [x]ContaCorrente
    [x]ContaPoupanca

[x]Pessoa (ABC)
    [x]Cliente
        [x]Cliente -> Conta

[x]Banco
    [x]Banco -> Cliente
    [x]Banco -> Conta

[x]cliente tem uma conta corrente ou poupança
[x]cliente pode sacar e depositar
[x]Conta corrente tem um limite extra
[x]classe Cliente herda da classe Pessoa
[x]Pessoa tem nome e idade (com getters)
[x]Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)

[x]Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    [x]ContaCorrente deve ter um limite extra
    [x]Contas têm agência, número da conta e saldo
    [x]Contas devem ter método para depósito
    [x]Conta (super classe) deve ter o método sacar abstrato (Abstração e
    [x]polimorfismo - as subclasses que implementam o método sacar)

[x]Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)

[x]Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    [x]Banco tem contas e clientes (Agregação)
    [x]Checar se a agência é daquele banco
    [x]Checar se o cliente é daquele banco
    [x]Checar se a conta é daquele banco

[x]Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método.




Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra.

Conta (ABC)
    ContaCorrente
    ContaPoupanca

Pessoa (ABC)
    Cliente
        Cliente -> Conta

Banco
    Banco -> Cliente
    Banco -> Conta

Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clientes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método.
"""
