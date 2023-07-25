from unittest import TestCase

from lpp.ast import (
  ExpressionStatement,
  Identifier,
  Integer,
  LetStatement,
  ReturnStatement,
  Program,
)
from lpp.token import (
  Token,
  TokenType
)

class ASTTest(TestCase):

  def test_let_statement(self) -> None:
    program: Program = Program(statements=[
      LetStatement(
        token=Token(TokenType.LET, literal='variable'),
        name=Identifier(
          token=Token(TokenType.IDENT, literal='mivar'),
          value='mi_var'
        ),
        value=Identifier(
          token=Token(TokenType.IDENT, literal='otra_variable'),
          value='otra_var'
        )
      )
    ])
    program_str = str(program)

    self.assertEqual(program_str, 'variable mi_var = otra_var;')

  def test_return_statement(self) -> None:
    program: Program = Program(statements=[
      ReturnStatement(
        token=Token(TokenType.RETURN, literal='regresa'),
        return_value=Identifier(
          token=Token(TokenType.IDENT, literal='foo'),
          value='foo'
        )
      ),
    ])
    program_str = str(program)

    self.assertEqual(program_str, 'regresa foo;')

  def test_identifier_expression(self) -> None:
    program: Program = Program(statements=[
      ExpressionStatement(
        token=Token(TokenType.IDENT, literal='foobar'),
        expression=Identifier(
          token=Token(TokenType.IDENT, literal='foobar'),
          value='foobar'
        )
      )
    ])
    program_str = str(program)

    self.assertEqual(program_str , 'foobar')

  def test_integer_expression(self) -> None:
    program: Program = Program(statements=[
      ExpressionStatement(
        token=Token(TokenType.INT, literal='5'),
        expression=Integer(
          token=Token(TokenType.INT, literal='5'),
          value=5
        )
      )
    ])
    program_str = str(program)

    self.assertEqual(program_str , '5')