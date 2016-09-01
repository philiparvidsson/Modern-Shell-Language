#-------------------------------------------------
# IMPORTS
#-------------------------------------------------

from . import core
from . import parser

#-------------------------------------------------
# CONSTANTS
#-------------------------------------------------

ADD        = "add"
ASSIGNMENT = "assignment"
CALL       = "call"
DIVIDE     = "divide"
IDENTIFIER = "identifier"
MULTIPLY   = "multiply"
NUMERAL    = "numeral"
STRING     = "string"
SUBTRACT   = "subtract"

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

def call(tokens):
    identifier_token = tokens.get_next()
    left_paren_token = tokens.get_next()

    arg_nodes = []

    arg_token = tokens.peek()
    while arg_token.kind != parser.RIGHT_PAREN:
        arg_node = expression(tokens)

        # Cannot use calls as args.
        assert arg_node.kind != CALL

        arg_nodes.append(arg_node)

        comma_token = tokens.peek()
        if comma_token.kind != parser.COMMA:
            break

        # Eat comma.
        tokens.get_next()

    right_paren_token = tokens.get_next()

    return Node(CALL, identifier_token.value, arg_nodes)

def expression(tokens):
    token = tokens.peek()

    result = None

    if token.kind == parser.LEFT_PAREN:
        tokens.get_next()
        result = expression(tokens)
        right_paren = tokens.get_next()
    elif token.kind == parser.IDENTIFIER:
        if tokens.peek(1).kind == parser.EQ_SIGN:
            result = assignment(tokens) # identifier = expr
        elif tokens.peek(1).kind == parser.LEFT_PAREN:
            result = call(tokens)
        else:
            tokens.get_next()
            result = Node(IDENTIFIER, token.value)
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
        elif token.kind == parser.MINUS:
            tokens.get_next()
            lhs = result
            rhs = expression(tokens)
            result = Node(SUBTRACT, "-", [lhs, rhs])
        elif token.kind == parser.ASTERISK:
            tokens.get_next()
            lhs = result
            rhs = expression(tokens)
            result = Node(MULTIPLY, "*", [lhs, rhs])
        elif token.kind == parser.SLASH:
            tokens.get_next()
            lhs = result
            rhs = expression(tokens)
            result = Node(DIVIDE, "/", [lhs, rhs])

    return result

def generate_ast(tokens):
    return expression(tokens)
