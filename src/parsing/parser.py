#--------------------------------------------------
# IMPORTS
#--------------------------------------------------

import mshl

from .node   import Node
from .syntax import PROGRAM, parse_expr

from lexing import lexemes

#--------------------------------------------------
# CONSTANTS
#--------------------------------------------------

DEFAULT_MAX_ERRORS = 10

#--------------------------------------------------
# CLASSES
#--------------------------------------------------

class Parser(object):
    def __init__(self, lexer):
        self.lexer = lexer

        self.errors = []
        self.max_errors = DEFAULT_MAX_ERRORS

        self.peeked_token = None

    def eat_whitespace(self, eat_semicolons=False):
        tok = self.peek_token()
        if eat_semicolons:
            cats = (lexemes.NEWLINE, lexemes.SEMICOLON)
        else:
            cats = (lexemes.NEWLINE,)
        while tok.category in cats:
            self.read_token()
            tok = self.peek_token()

    def expect(self, *args):
        tokens = []

        for lexeme in args:
            token = self.read_token()

            if token.category != lexeme:
                mshl.error('expected {}'.format(lexeme), token)

            tokens.append(token)

        if len(tokens) == 1:
            tokens = tokens[0]

        return tokens

    def generate_ast(self):
        expressions = []

        while True:
            self.eat_whitespace(eat_semicolons=True)
            expression = self.parse_expression()

            if not expression:
                break

            expressions.append(expression)

        return Node(PROGRAM, children=expressions)

    def parse_expression(self):
        tok = self.peek_token()
        while tok.category == lexemes.NEWLINE:
            self.read_token()
            tok = self.peek_token()

        return parse_expr(self)

    def peek_token(self):
        if not self.peeked_token:
            self.peeked_token = self.read_token()

        return self.peeked_token

    def read_token(self):
        if self.peeked_token:
            tok = self.peeked_token
            self.peeked_token = None
            return tok

        tok = self.lexer.read_token()
        while tok.category == lexemes.COMMENT:
            tok = self.lexer.read_token()
        #if tok.category == lexemes.SLASH_2:
        #    self.lexer.read_token()
        #    while tok.category not in (lexemes.EOF, lexemes.NEWLINE):
        #        tok = self.lexer.read_token()
        #elif tok.category == lexemes.SLASH_ASTERISK:
        #    self.lexer.read_token()
        #    while tok.category not in (lexemes.ASTERISK_SLASH, lexemes.EOF):
        #        tok = self.lexer.read_token()
        #    tok = self.lexer.read_token()

        return tok
