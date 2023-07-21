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
