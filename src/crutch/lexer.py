#-------------------------------------------------
# IMPORTS
#-------------------------------------------------

from . import core
from . import parser

#-------------------------------------------------
# CONSTANTS
#-------------------------------------------------

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
    literal_token    = tokens.get_next()

    identifier_node = Node(IDENTIFIER, identifier_token.value)
    literal_node    = Node(NUMERAL if literal_token.kind == parser.NUMERAL else STRING, literal_token.value)
    assignment_node = Node(ASSIGNMENT, children=[identifier_node, literal_node])

    return assignment_node

def expression(tokens):
    token = tokens.peek()

    if token.kind == parser.IDENTIFIER:
        if tokens.peek(1).kind == parser.EQ_SIGN:
            return assignment(tokens) # identifier = expr
    elif token.kind == parser.NUMERAL:
        return Node(NUMERAL, token.value)
    elif token.kind == parser.STRING:
        return Node(STRING, token.value)

def generate_ast(tokens):
    return expression(tokens)
