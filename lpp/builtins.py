from typing import (
  cast,
  Dict,
)

from lpp.object import (
  Builtin,
  Error,
  Integer,
  Object,
  String,
)


_UNSUPPORTED_ARGUMENT_TYPE = 'Argumento para {}() sin soporte, se recibió {}'
_WRONG_NUMBER_OF_ARGS = 'Número incorrecto de argumentos para {}(), se recibieron {}, se requieren {}'


def longitud(*args: Object) -> Object:
  if len(args) != 1:
    return Error(_WRONG_NUMBER_OF_ARGS.format('longitud', str(len(args)), '1'))
  elif type(args[0]) == String:
    argument = cast(String, args[0])
    return Integer(len(argument.value))
  return Error(_UNSUPPORTED_ARGUMENT_TYPE.format('longitud', str(args[0].type().name)))


BUILTINS: Dict[str, Builtin] = {
  'longitud': Builtin(fn=longitud),
}