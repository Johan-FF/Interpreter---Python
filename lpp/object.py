from typing import (
  Any,
  Dict,
  List,
)
from abc import (
  ABC,
  abstractmethod,
)
from enum import (
  auto,
  Enum,
)

from lpp.ast import (
  BlockStatement,
  Identifier,
)


class Environment(Dict):
  def __init__(self, outer = None) -> None:
    self._store: Dict[Any, Any] = dict()
    self._outer = outer

  def __getitem__(self, key: Any) -> Any:
    try:
      return self._store[key]
    except KeyError as e:
      if self._outer is not None:
        return self._outer[key]
      raise

  def __setitem__(self, key: Any, value: Any) -> None:
    self._store[key] = value

  def __delitem__(self, key: Any) -> None:
    del self._store[key]


class ObjectType(Enum):
  BOOLEAN = auto()
  ERROR = auto()
  FUNCTION = auto()
  INTEGER = auto()
  NULL = auto()
  RETURN = auto()

class Object(ABC):
  @abstractmethod
  def type(self) -> ObjectType:
    pass

  @abstractmethod
  def inspect(self) -> str:
    pass


class Integer(Object):
  def __init__(self, value: int) -> None:
    self.value = value

  def type(self) -> ObjectType:
    return ObjectType.INTEGER

  def inspect(self) -> str:
    return str(self.value)

class Boolean(Object):
  def __init__(self, value: bool) -> None:
    self.value = value

  def type(self) -> ObjectType:
    return ObjectType.BOOLEAN

  def inspect(self) -> str:
    return 'verdadero' if self.value else 'falso'

class Return(Object):
  def __init__(self, value: Object) -> None:
    self.value = value

  def type(self) -> ObjectType:
    return ObjectType.RETURN

  def inspect(self) -> str:
    return self.value.inspect()

class Function(Object):
  def __init__(self,
      parameters: List[Identifier],
      body: BlockStatement,
      env: Environment) -> None:
    self.parameters = parameters
    self.body = body
    self.env = env

  def type(self) -> ObjectType:
    return ObjectType.FUNCTION

  def inspect(self) -> str:
    params: str = ', '.join([str(param) for param in self.parameters])

    return 'procedimiento({}) {{\n{}\n}}'.format(params, str(self.body))

class Error(Object):
  def __init__(self, message: str) -> None:
    self.message = message

  def type(self) -> ObjectType:
    return ObjectType.ERROR

  def inspect(self) -> str:
    return f'Error: {self.message}'

class Null(Object):
  def type(self) -> ObjectType:
    return ObjectType.NULL

  def inspect(self) -> str:
    return 'nulo'