#--------------------------------------------------
# IMPORTS
#--------------------------------------------------

import copy

from .node import Node

from lexing import lexemes

#--------------------------------------------------
# CONSTANTS
#--------------------------------------------------

ADD        = 'add'
ASSIGNMENT = 'assignment'
IDENTIFIER = 'identifier'
INTEGER    = 'integer'
MULTIPLY   = 'multiply'
PROGRAM    = 'program'
STRING     = 'string'

#--------------------------------------------------
# GLOBALS
#--------------------------------------------------

rules = dict()

#--------------------------------------------------
# FUNCTIONS
#--------------------------------------------------

def rule(lexeme):
    def decorator(func):
        rules[lexeme] = func
        return func

    return decorator

@rule(lexemes.ASTERISK)
def parse_asterisk(parser, previous_node):
    # Consume asterisk.
    asterisk = parser.read_token()

    if not previous_node:
        parser.error("unexpected token: *", asterisk)

    left_hand_side  = previous_node
    right_hand_side = parser.parse_expression()

    return Node(MULTIPLY, children=[left_hand_side, right_hand_side])

@rule(lexemes.EQUALS_SIGN)
def parse_assignment(parser, previous_node):
    identifier = previous_node

    # Consume the equals sign token.
    token = parser.read_token()

    if not identifier:
        parser.error("unexpected token: =", token)
    elif identifier.construct != IDENTIFIER:
        parser.error("can only assign to variables", token)

    expression = parser.parse_expression()

    node = Node(ASSIGNMENT, children=[identifier, expression])

    return node

@rule(lexemes.IDENTIFIER)
def parse_identifier(parser, previous_node):
    token = parser.read_token()

    if previous_node:
        parser.error("identifier was unexpected here", token)

    return Node(IDENTIFIER, str(token.lexeme))

@rule(lexemes.INTEGER)
def parse_integer(parser, previous_node):
    token = parser.read_token()

    if previous_node:
        parser.error("integer was unexpected here", token)

    return Node(INTEGER, int(token.lexeme))

@rule(lexemes.LEFT_PARENTHESIS)
def parse_left_parenthesis(parser, previous_node):
    assert previous_node is None

    # Consume the left parenthesis.
    parser.read_token()

    node = parser.parse_expression()

    # Make sure we end the exprssion with a right parenthesis.
    token = parser.read_token()
    if token.category != lexemes.RIGHT_PARENTHESIS:
        s = "expected right parenthesis but got {}"
        parser.error(s.format(token.lexeme), token)

    return node

@rule(lexemes.PLUS_SIGN)
def parse_plus_sign(parser, previous_node):
    # Consume plus sign.
    plus_sign = parser.read_token()

    if not previous_node:
        parser.error("unexpected token: +", plus_sign)

    left_hand_side  = previous_node
    right_hand_side = parser.parse_expression()

    return Node(ADD, children=[left_hand_side, right_hand_side])

@rule(lexemes.STRING)
def parse_string(parser, previous_node):
    token = parser.read_token()
    value = str(token.lexeme)

    if previous_node:
        parser.error("string was unexpected here", token)

    if not value.startswith('"') or not value.endswith('"'):
        parser.error("unterminated string", token)

    value = value[1:-1]

    return Node(STRING, value)
