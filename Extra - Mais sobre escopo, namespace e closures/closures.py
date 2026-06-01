#
# Closures em Python
#
# O que são closures?
# Closures ocorrem quando funções internas, definidas dentro de outras funções,
# referenciam variáveis livres do seu escopo. Variáveis livres são as
# variáveis que não foram definidas no escopo da função interna (são da função
# externa).
# Se a função externa retornar apenas a referência da função interna, então
# o interpretador precisará atrelar quaisquer referências a variáveis livres
# que a função interna precisar para que ela possa ser executada corretamente.
# São muito usados em programação funcional, decoradores de função e algoritmos
# em geral.


def externa(a):
    # Enclosing é a função externa
    def interna(b):
        # Função interna precisa de `a`
        return f"{a} {b}"

    return interna  # Função interna não executada(o python pensa, eu vou executar depois :)
    # Retorna uma referência para a função interna(b)

imcompleto = externa("Luiz") # basicamente closures precisam lembrar desse argumento passado pra função externa(fica armazenado na call stack)
completo = imcompleto("Otávio") # agora vai usar o argumento salvo na call stack e terminar a execução da função interna

# print(completo)

#
# ** Quando usar closures?
#
# - Para manter estados simples sem usar classes
# - Para criar fábricas (factories) de funções
# - Para encapsular o código e esconder nomes importantes de escopos amplos
# - Para usar funções de callback (onde algo é feito por etapas)
# - Para decoradores de função em Python
# - Para programação funcional e algoritmos em geral
#


################################################################################


from utils import Logger


def make_logger(name: str, color: str, icon: str = "…") -> Logger:
    def logger(log: str) -> None:
        log_name = f"{color}[{name.upper(): <7}] "
        print(f"{log_name} {icon} {log}\033[0m")

    return logger


debug = make_logger("debug", "\033[032m", icon="…")
info = make_logger("info", "\033[034m", icon="✔")
warning = make_logger("warning", "\033[033m", icon="⚠")
error = make_logger("error", "\033[031m", icon="✘")

# print()
# debug("Esse é um log de DEBUG")
# info("Aconteceu alguma coisa no código")
# warning("OPA!!! PRESTENÇÃO MINNINUUUUU...")
# error("Te falei que ia dar ruim...")
# debug("Esse é um log de DEBUG")
# debug("Esse é um log de DEBUG")
# print()


################################################################################


#
# Exemplos de closures
#
from collections.abc import Callable
from typing import Protocol


# Factory (fábrica de funções)
def make_multiplier(multiplier: float, /) -> Callable[[float], float]:
    def multiplier_times(multiplicand: float, /) -> float:
        return multiplicand * multiplier

    return multiplier_times


# print("\nMultiplicadores")
# times_two = make_multiplier(2)  # Função interna precisará lembrar do 2
# times_three = make_multiplier(3)  # Nesse caso do 3

# print("3 * 2 =   ", times_two(3))  # 3 * [2] = 6 - [2] lembrado
# print("3 * 5 =   ", times_three(5))  # 5 * [3] = 15 - [3] lembrado

################################################################################


# Validador simples
def make_lt_checker(min_value: int) -> Callable[[int], bool]:
    def is_lt(value: int) -> bool:
        return value < min_value

    return is_lt


# print("\nValidatores simples")
# lt_ten = make_lt_checker(10)  # 10 precisa ser lembrado

# print("30 < 10   ", lt_ten(30))  # 30 é menor do que 10? False
# print("9 < 10   ", lt_ten(9))  # 9 é menor do que 10? True

################################################################################

"""
Callback é quando você executa uma ação e depois de executada você quer fazer outra coisa na sequência
"""
def with_callback(value: str, callback: Callable[[str], str]) -> Callable[[], str]:
    # Você também poderia realizar algo aqui
    def runner() -> str:
        print(f"Realizando alguma operação com o valor {value!r}")
        return callback(value)

    return runner


def my_callback(value: str) -> str:
    print(f"Valor {value!r} recebido no callback")
    return value + " (callback executed)"


# print("\nCallback")

# execute_operation = with_callback("## Exemplo ##", callback=my_callback)
# result = execute_operation()
# print(f"Callback:    {result!r}")


################################################################################


class Operation[**P, R](Protocol):
    def __call__(self, *args: P.args, **kwargs: P.kwargs) -> R: ...


def cacher[**P, R](callback: Operation[P, R]) -> Callable[P, R]:
    cached_params: dict[tuple[object, ...], R] = {}

    def closure(*args: P.args, **kwargs: P.kwargs) -> R:
        if args in cached_params:
            result = cached_params[args]
            print(f"Cacher found result {result!r}")
        else:
            result = callback(*args, **kwargs)
        cached_params[args] = result

        return result

    return closure


def operation(*args: str) -> list[str]:
    import time

    values: list[str] = []

    for arg in args:
        print(f"Fazendo algo complexo ou demorado com {arg!r}...")
        time.sleep(1)
        values.append(arg)

    return values


# print("\nCacher")
# operation_cached = cacher(operation)

# op1 = operation_cached("a", "b", "c")
# op2 = operation_cached("a", "b", "c")  # em cache

# op4 = operation_cached("b", "b", "c")
# op5 = operation_cached("b", "b", "c")  # em cache

################################################################################


@cacher
def get_from_db(id: int, /) -> str:
    import time

    names = ["Luiz", "Maria", "Helena", "Letícia"]

    print(f"Returning value for ID {id}")
    time.sleep(2)
    return names[id]


# print("\nCacher Decorator")

# print(get_from_db(1))
# print(get_from_db(1))
# print(get_from_db(0))
# print(get_from_db(2))
# print(get_from_db(0))
# print(get_from_db(2))
# print(get_from_db(0))
# print(get_from_db(2))
# print(get_from_db(0))
# print(get_from_db(2))


# ** Introspecção de closures

from collections.abc import Callable


def enclosing(a: str) -> Callable[[str], str]:
    def closure(b: str) -> str:
        return f"{a} {b}"

    return closure


same_closure = enclosing("João")  # aqui está o closure
this_is_result_str = same_closure("Otávio")  # isso é uma str

print()
print("variáveis do ponto de vista da função enclosing")
# Como ver dados da função externa
# Variáveis exclusivamente locais
print("Varnames [Local    ]  ", enclosing.__code__.co_varnames)
# Variáveis do enclosing usadas nessa função
print("Freevars [Enclosing]  ", enclosing.__code__.co_freevars)
# Variáveis dessa função usadas em funções internas
print("Cellvars [Usadas   ]  ", enclosing.__code__.co_cellvars)
# Células da closure se existir
print("Closure  [Closure  ]  ", enclosing.__closure__)

print()
print()
print("variáveis do ponto de vista da função same_closure")
# Como ver dados da função interna
# Variáveis exclusivamente locais
print("Varnames [Local    ]  ", same_closure.__code__.co_varnames)
# Variáveis do enclosing usadas nessa função
print("Freevars [Enclosing]  ", same_closure.__code__.co_freevars)
# Variáveis dessa função usadas em funções internas
print("Cellvars [Usadas   ]  ", same_closure.__code__.co_cellvars)
# Células da closure se existir
print("Closure  [Closure  ]  ", same_closure.__closure__[0].cell_contents)


################################################################################
