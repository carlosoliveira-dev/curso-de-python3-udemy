# Valores padrão e field em dataclasses
# doc: https://docs.python.org/3/library/dataclasses.html
from dataclasses import dataclass, field, fields


# field é usado para definir um objeto padrão mutável em uma dataclass
@dataclass
class Pessoa:
    nome: str = field(
        default='MISSING', repr=True
    )
    sobrenome: str = 'Not sent'
    idade: int = 100
    enderecos: list[str] = field(default_factory=list)


if __name__ == '__main__':
    p1 = Pessoa()
    print('FIELDS')
    print(*fields(p1), sep='\n\n')
    print()

    print(f'{p1=}')
