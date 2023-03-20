from typing import (
    Any,
    NewType,
    Iterable
    )

from collections.abc import Callable


'''Primitivos'''

integer: int = 10

floa: float = 10.0

booll: bool = True

string: str = 'str'

set1: set = {1, 2, 3}


'''Sequencias'''

list1: list = [1, 2, 3]

list2: list[int] = [1, 2, 3]  # lista apenas de inteiros

# "|" tem funcao de "or"
list3: list[int | str] = [1, 2, 'tres']

tup: tuple = (1, 2, 3)

# com tuplas deve-se especificar o tipo de cada argumento
tup2: tuple[int, int, int] = (1, 2, 3)


'''Dicionarios e conjuntos'''

# com dicionarios deve-se especificar tipo de chave e valor
person: dict[str, str | int] = {'nome': 'gustavo', 'idade': 18}

# "Any" recebe qualquer valor (má pratica)
person2: dict[str, Any] = {'nome': 'gustavo', 'idade': 18}

person3: dict[str, str | int | list[int]] = {'nome': 'gus', 'idade': 18}

MyDict = dict[str, str | int | list[int]]  # alias para tipagem

person4: MyDict = {'nome': 'gustavo', 'idade': 18}


'''Criacao de novo tipo'''

UserId = NewType('UserId', int)  # nome do tipo, tipo do tipo

user_id = UserId(345678)


'''Funcoes'''

# Callable[[], None]:
# dentro de colchetes [] -> argumentos
# agr fora dos colchetes -> retorno da funcao


def return_function(funcction: Callable[[], None]) -> Callable:
    return funcction


def say_hi():
    print('Hi')


return_function(say_hi())


def iterate(iterable: Iterable[int]) -> Iterable:
    return [x for x in iterable]


print(iterate([1, 2, 3]))


'''Classes:'''


class People:
    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name: str = first_name
        self.last_name: str = last_name

    def fala(self) -> None:
        print(f'{self.first_name} {self.last_name} is talking...')


# classes pot si só ja sáo um tipo
def say_my_name(person: People) -> str:
    return person.first_name


print(say_my_name(People('Gustavo', 'Silva')))
