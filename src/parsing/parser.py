#--------------------------------------------------
# IMPORTS
#--------------------------------------------------

import inspect

from .node   import Node
from .syntax import PROGRAM, rules

#--------------------------------------------------
# CLASSES
#--------------------------------------------------

class Parser(object):
    def __init__(self, lexer):
        self.lexer  = lexer
        self.syntax = dict()
        self.tokens = []

    def error(self, message, token=None):
        print "implement Parser.error pls"

    def generate_abstract_syntax_tree(self):
        expressions = []

        while True:
            expression = self.parse_expression()

            if not expression:
                break

            expressions.append(expression)

        return Node(PROGRAM, children=expressions)

    def parse_expression(self):
        parse_fn = None
        token = self.read_token()

        if not token:
            return None

        tokens = token,
        while True:
            sequence = tuple(map(lambda token: token.category, tokens))

            if sequence in rules:
                parse_fn = rules[sequence]
            elif parse_fn:
                break

            token = self.read_token()

            # No more tokens in the source.
            if not token:
                break

            tokens += token,

        for token in tokens:
            self.putback(token)

        if parse_fn:
            return parse_fn(self)
        else:
            self.error("cant parse this shit")

    def read_token(self):
        if len(self.tokens) > 0:
            # Tokens have been put back, so retrieve them again before reading
            # new tokens from the lexer.
            return self.tokens.pop(0)

        return self.lexer.read_token()

    def putback(self, token):
        self.tokens.append(token)
