#--------------------------------------------------
# IMPORTS
#--------------------------------------------------

import inspect

from .error  import Error
from .node   import Node
from .syntax import PROGRAM, rules

from lexing.lexemes import EOF, NEWLINE

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

    def error(self, message, token=None):
        e = Error(message, token)
        self.errors.append(e)

        print e

    def generate_abstract_syntax_tree(self):
        expressions = []

        while True:
            expression = self.parse_expression()

            if not expression:
                break

            expressions.append(expression)

        return Node(PROGRAM, children=expressions)

    def parse_expression(self):
        node = None

        while len(self.errors) < self.max_errors:
            token = self.peek_token()
            if token.category == EOF:
                break

            if token.category == NEWLINE:
                self.read_token()
                continue

            if not token.category in rules:
                if not node:
                    s = "unexpected token encountered: {}"
                    self.error(s.format(token.category), token)
                break

            parse_fn = rules[token.category]
            node = parse_fn(self, node)
            if node:
                node.token = token

            if self.peek_token().category == NEWLINE:
                break

        return node

    def peek_token(self):
        if not self.peeked_token:
            self.peeked_token = self.read_token()


        return self.peeked_token

    def read_token(self):
        if self.peeked_token:
            token = self.peeked_token
            self.peeked_token = None
            return token

        return self.lexer.read_token()

#--------------------------------------------------
# FUNCTIONS
#--------------------------------------------------

#def prune_tree(root):
#    if not root.children:
#        return
#
#    root.children = filter(lambda child: child.construct, root.children)
#
#    for child in root.children:
#        prune_tree(child)
