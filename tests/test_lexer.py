from unittest import TestCase
from typing import List

from lpp.token import (
  Token,
  TokenType
)
from lpp.lexer import Lexer

class LexerTest(TestCase):
  def _get_execute_tokens(self, source: str, max: int) -> List[Token]:
    lexer: Lexer = Lexer(source)

    tokens: List[Token] = []
    for i in range(max):
      tokens.append(lexer.next_token())
    return tokens

  def test_illegal(self) -> None:
    source: str = '¡¿@'
    tokens: List[Token] = self._get_execute_tokens(
      source, len(source)
    )
    expected_tokens: List[Token] = [
      Token(TokenType.ILLEGAL, '¡'),
      Token(TokenType.ILLEGAL, '¿'),
      Token(TokenType.ILLEGAL, '@'),
    ]

    self.assertEqual(tokens, expected_tokens)

  def test_one_character_operation(self) -> None:
    source: str = '=+'
    tokens: List[Token] = self._get_execute_tokens(
      source, len(source)
    )
    expected_tokens: List[Token] = [
      Token(TokenType.ASSIGN, '='),
      Token(TokenType.PLUS, '+'),
    ]

    self.assertEqual(tokens, expected_tokens)

  def test_end_of_file(self) -> None:
    source: str = ''
    tokens: List[Token] = self._get_execute_tokens(
      source, 1
    )
    expected_tokens: List[Token] = [
      Token(TokenType.EOF, ''),
    ]

    self.assertEqual(tokens, expected_tokens)

  def test_delimiters(self) -> None:
    source: str = '(){},;'
    tokens: List[Token] = self._get_execute_tokens(
      source, len(source)
    )
    expected_tokens: List[Token] = [
      Token(TokenType.LPAREN, '('),
      Token(TokenType.RPAREN, ')'),
      Token(TokenType.LBRACE, '{'),
      Token(TokenType.RBRACE, '}'),
      Token(TokenType.COMMA, ','),
      Token(TokenType.SEMICOLON, ';'),
    ]

    self.assertEqual(tokens, expected_tokens)

  def test_assignment(self) -> None:
    source: str = 'variable cinco = 5;'
    tokens: List[Token] = self._get_execute_tokens(
      source, 5
    )
    expected_tokens: List[Token] = [
      Token(TokenType.LET, 'variable'),
      Token(TokenType.IDENT, 'cinco'),
      Token(TokenType.ASSIGN, '='),
      Token(TokenType.INT, '5'),
      Token(TokenType.SEMICOLON, ';'),
    ]

    self.assertEqual(tokens, expected_tokens)

  def test_function_declaration(self) -> None:
    source: str = '''
      variable suma = procedimiento(x, y) {
        x + y;
      };
    '''
    tokens: List[Token] = self._get_execute_tokens(
      source, 16
    )
    expected_tokens: List[Token] = [
      Token(TokenType.LET, 'variable'),
      Token(TokenType.IDENT, 'suma'),
      Token(TokenType.ASSIGN, '='),
      Token(TokenType.FUNCTION, 'procedimiento'),
      Token(TokenType.LPAREN, '('),
      Token(TokenType.IDENT, 'x'),
      Token(TokenType.COMMA, ','),
      Token(TokenType.IDENT, 'y'),
      Token(TokenType.RPAREN, ')'),
      Token(TokenType.LBRACE, '{'),
      Token(TokenType.IDENT, 'x'),
      Token(TokenType.PLUS, '+'),
      Token(TokenType.IDENT, 'y'),
      Token(TokenType.SEMICOLON, ';'),
      Token(TokenType.RBRACE, '}'),
      Token(TokenType.SEMICOLON, ';'),
    ]

    self.assertEqual(tokens, expected_tokens)

  def test_function_call(self) -> None:
    source: str = 'variable resultado = suma(dos, tres);'
    tokens: List[Token] = self._get_execute_tokens(
      source, 10
    )
    expected_tokens: List[Token] = [
      Token(TokenType.LET, 'variable'),
      Token(TokenType.IDENT, 'resultado'),
      Token(TokenType.ASSIGN, '='),
      Token(TokenType.IDENT, 'suma'),
      Token(TokenType.LPAREN, '('),
      Token(TokenType.IDENT, 'dos'),
      Token(TokenType.COMMA, ','),
      Token(TokenType.IDENT, 'tres'),
      Token(TokenType.RPAREN, ')'),
      Token(TokenType.SEMICOLON, ';'),
    ]

    self.assertEqual(tokens, expected_tokens)