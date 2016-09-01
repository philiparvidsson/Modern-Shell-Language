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
# HELPER FUNCTIONS
#-------------------------------------------------

def print_node(node, level):
    kind = node.kind[0:3]

    tab = "    " * (level-1)
    arrow = "|-- " if level > 0 else ""
    nodeinfo = "[{}: {}]".format(kind, node.value)

    print(tab + arrow + nodeinfo)
    return len(tab+arrow+nodeinfo)

def visualize(node, level=0):
    print_node(node, level)
    for child in node.children:
        visualize(child, level+1)

def max_len(node, level=0):
    _max = level*4 + len(node.value) + 7
    for child in node.children:
        _temp = max_len(child, level+1)
        _max = _max if _temp < _max else _temp

    return _max

def draw_ast_tree(node):
    maxlen = max_len(node)
    print("\n-----AST" + "-" * (maxlen-6))
    visualize(node)
    print("--------" + "-" * (maxlen-6) + "\n")

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

    right_paren_token = tokens.get_next()

    return Node(CALL, identifier_token.value)

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
