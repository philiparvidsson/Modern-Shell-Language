#-------------------------------------------------
# IMPORTS
#-------------------------------------------------

from parse import Token

#-------------------------------------------------
# CONSTANTS
#-------------------------------------------------

(ASSIGNMENT, NUMERAL, IDENTIFIER) = range(3)

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
        return "Node(value={}, children={})".format(self.value, children)

#-------------------------------------------------
# FUNCTIONS
#-------------------------------------------------

def peek_token(tokens, num_to_skip = 0):
    return tokens[num_to_skip]

def assignment(tokens):
    ident_tok  = tokens[0]
    assign_tok = tokens[1]

    tokens = tokens[2:]

    ident_node = Node(IDENTIFIER, ident_tok.value)
    expr_node = expression(tokens)

    return Node(ASSIGNMENT, children = [ident_node, expr_node])


def expression(tokens):
    token = peek_token(tokens)

    if (token.kind == Token.IDENTIFIER):
        if (peek_token(tokens, 1).kind == Token.ASSIGNMENT):
            return assignment(tokens)
    elif (token.kind == Token.NUMERAL):
        return Node(NUMERAL, token.value)

    return None

def from_tokens(tokens):
    root = expression(tokens)

    return root
