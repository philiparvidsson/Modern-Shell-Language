#-------------------------------------------------
# IMPORTS
#-------------------------------------------------

from . import core
from . import parser

#-------------------------------------------------
# CONSTANTS
#-------------------------------------------------

ADD         = "add"
ASSIGNMENT  = "assignment"
IDENTIFIER  = "identifier"
NUMERAL     = "numeral"
STRING      = "string"

#-------------------------------------------------
# CLASSES
#-------------------------------------------------

class Node(object):
    def __init__(self, kind, value = "", children = []):
        self.parent   = None
        self.children = children

        self.kind  = kind
        self.value = value

    def __str__(self):
        children = []
        for child in self.children:
            children += [str(child)]
        return "Node(kind={}, value={}, children={})".format(self.kind, self.value, children)

#-------------------------------------------------
# FUNCTIONS
#-------------------------------------------------

def assignment(tokens):
    identifier_token = tokens.get_next()
    assignment_token = tokens.get_next()

    identifier_node = Node(IDENTIFIER, identifier_token.value)
    expression_node = expression(tokens)
    assignment_node = Node(ASSIGNMENT, children=[identifier_node, expression_node])

    return assignment_node

def expression(tokens):
    token = tokens.peek()

    result = None

    if token.kind == parser.IDENTIFIER:
        if tokens.peek(1).kind == parser.EQ_SIGN:
            result = assignment(tokens) # identifier = expr
    elif token.kind == parser.NUMERAL:
        tokens.get_next()
        result = Node(NUMERAL, token.value)
    elif token.kind == parser.STRING:
        tokens.get_next()
        result = Node(STRING, token.value)

    token = tokens.peek()
    if token:
        if token.kind == parser.PLUS:
            tokens.get_next()
            lhs = result
            rhs = expression(tokens)
            result = Node(ADD, "+", [lhs, rhs])

    return result

def generate_ast(tokens):
    return expression(tokens)
