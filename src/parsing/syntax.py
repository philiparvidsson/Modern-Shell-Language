#--------------------------------------------------
# IMPORTS
#--------------------------------------------------

from .node import Node

from lexing import lexemes

#--------------------------------------------------
# CONSTANTS
#--------------------------------------------------

ASSIGNMENT = 'assignment'
IDENTIFIER = 'identifier'
INTEGER    = 'integer'
PROGRAM    = 'program'
STRING     = 'string'

#--------------------------------------------------
# GLOBALS
#--------------------------------------------------

rules = dict()

#--------------------------------------------------
# FUNCTIONS
#--------------------------------------------------

def rule(*args):
    def decorator(func):
        rules[args] = func
        return func

    return decorator

@rule(lexemes.IDENTIFIER)
def parse_identifier(parser):
    return Node(IDENTIFIER, str(parser.read_token().lexeme))

@rule(lexemes.INTEGER)
def parse_integer(parser):
    return Node(INTEGER, int(parser.read_token().lexeme))

@rule(lexemes.STRING)
def parse_string(parser):
    token = parser.read_token()
    value = str(token.lexeme)

    if not value.startswith('"') or not value.endswith('"'):
        parser.error("unterminated string", token)

    value = value[1:-1]

    return Node(STRING, value)

@rule(lexemes.IDENTIFIER, lexemes.EQUALS_SIGN)
def parse_assignment(parser):
    identifier = Node(IDENTIFIER, parser.read_token().lexeme)

    # Consume the equals sign token.
    equals_sign = parser.read_token()

    expression = parser.parse_expression()

    return Node(ASSIGNMENT, lexemes.EQUALS_SIGN, [identifier, expression])
