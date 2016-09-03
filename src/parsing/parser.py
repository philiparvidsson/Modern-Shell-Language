#--------------------------------------------------
# IMPORTS
#--------------------------------------------------

import inspect

from .error  import Error
from .node   import Node
from .syntax import PROGRAM, rules

from lexing.lexemes import EOF, NEWLINE

#--------------------------------------------------
# CLASSES
#--------------------------------------------------

class Parser(object):
    def __init__(self, lexer):
        self.lexer         = lexer
        self.previous_node = None
        self.tokens        = []

    def error(self, message, token=None):
        e = Error(message, token)
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

        while True:
            token = self.read_token()
            if token.category == EOF:
                break

            if token.category == NEWLINE:
                if node:
                    self.putback(token)
                    break
                continue

            if not token.category in rules:
                self.putback(token)
                if not node:
                    self.error('something is afuck', token)
                break

            parse_fn = rules[token.category]
            self.putback(token)
            node = parse_fn(self, node)
            if node:
                node.token = token

        return node

    def read_token(self):
        if len(self.tokens) > 0:
            # Tokens have been put back, so retrieve them again before reading
            # new tokens from the lexer.
            return self.tokens.pop(0)

        return self.lexer.read_token()

    def putback(self, token):
        self.tokens.append(token)

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
