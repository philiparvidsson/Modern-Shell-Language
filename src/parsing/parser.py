#--------------------------------------------------
# IMPORTS
#--------------------------------------------------

import inspect

from .error  import Error
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

    def err(self, message, token=None):
        e = Error(message, token)
        self.errors.append(e)

        print e

    def eat_whitespace(self):
        tok = self.peek_token()
        while tok.category in (lexemes.NEWLINE, lexemes.SEMICOLON):
            self.read_token()
            tok = self.peek_token()

    def expect(self, *args):
        tokens = []

        for lexeme in args:
            token = self.read_token()

            if token.category != lexeme:
                self.err("expected {}".format(lexeme), token)

            tokens.append(token)

        if len(tokens) == 1:
            tokens = tokens[0]

        return tokens

    def generate_abstract_syntax_tree(self):
        expressions = []

        while True:
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
            print tok
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

        print tok
        return tok
