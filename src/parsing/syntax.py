#--------------------------------------------------
# IMPORTS
#--------------------------------------------------

import copy

from .node import Node

from lexing import lexemes

#--------------------------------------------------
# CONSTANTS
#--------------------------------------------------

ADD                = 'add'
ASSIGNMENT         = 'assignment'
DIVIDE             = 'divide'
END                = 'end'
FUNCTION           = 'function'
FUNCTION_ARGUMENTS = 'function arguments'
FUNCTION_BODY      = 'function body'
IDENTIFIER         = 'identifier'
INTEGER            = 'integer'
MULTIPLY           = 'multiply'
PROGRAM            = 'program'
STRING             = 'string'
SUBTRACT           = 'subtract'

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
        return

    left_hand_side  = previous_node
    right_hand_side = parser.parse_expression()

    if not right_hand_side:
        parser.error("expected: expression", asterisk)
        return

    return Node(MULTIPLY, children=[left_hand_side, right_hand_side])

@rule(lexemes.END)
def parse_end(parser, previous_node):
    token = parser.read_token()

    if previous_node:
        parser.error("end was unexpected here", token)
        return

    return Node(END)

@rule(lexemes.EQUALS_SIGN)
def parse_assignment(parser, previous_node):
    identifier = previous_node

    # Consume the equals sign token.
    token = parser.read_token()

    if not identifier:
        parser.error("unexpected token: =", token)
        return
    elif identifier.construct != IDENTIFIER:
        parser.error("can only assign to variables", token)
        return

    expression = parser.parse_expression()

    node = Node(ASSIGNMENT, children=[identifier, expression])

    return node

@rule(lexemes.FUNCTION)
def parse_func(parser, previous_node):
    token = parser.read_token()

    if previous_node:
        parser.error("function was unexpected here", token)
        return

    function_name = str(parse_identifier(parser, None).data)

    token = parser.read_token()
    if token.category != lexemes.LEFT_PARENTHESIS:
        parser.error("expected left parenthesis", token)
        return

    arguments = Node(FUNCTION_ARGUMENTS, children=[])
    while True:
        token = parser.peek_token()

        if token.category == lexemes.RIGHT_PARENTHESIS:
            break

        node = parse_identifier(parser, None)
        arguments.children.append(node)


        token = parser.peek_token()
        token = parser.peek_token()
        if token.category == lexemes.RIGHT_PARENTHESIS:
            break

        if token.category != lexemes.COMMA:
            parser.error("expected comma or right parenthesis", token)
            return

        parser.read_token()

    token = parser.read_token()
    if token.category != lexemes.RIGHT_PARENTHESIS:
        parser.error("expected right parenthesis", token)
        return

    body = Node(FUNCTION_BODY, children=[])
    while True:
        node = parser.parse_expression()
        if node.construct == END:
            break
        body.children.append(node)

    return Node(FUNCTION, function_name, children=[arguments, body])



@rule(lexemes.IDENTIFIER)
def parse_identifier(parser, previous_node):
    token = parser.read_token()

    if previous_node:
        parser.error("identifier was unexpected here", token)
        return

    return Node(IDENTIFIER, str(token.lexeme))

@rule(lexemes.INTEGER)
def parse_integer(parser, previous_node):
    token = parser.read_token()

    if previous_node:
        parser.error("integer was unexpected here", token)
        return

    return Node(INTEGER, int(token.lexeme))

@rule(lexemes.LEFT_PARENTHESIS)
def parse_left_parenthesis(parser, previous_node):
    # Consume minus sign.
    token = parser.read_token()

    if not previous_node:
        parser.error("unexpected token: (", token)
        return

    node = parser.parse_expression()

    # Make sure we end the exprssion with a right parenthesis.
    token = parser.read_token()
    if token.category != lexemes.RIGHT_PARENTHESIS:
        s = "expected right parenthesis but got {}"
        parser.error(s.format(token.lexeme), token)
        return

    return node

@rule(lexemes.MINUS_SIGN)
def parse_slash(parser, previous_node):
    # Consume minus sign.
    token = parser.read_token()

    if not previous_node:
        parser.error("unexpected token: -", token)
        return

    left_hand_side  = previous_node
    right_hand_side = parser.parse_expression()

    if not right_hand_side:
        parser.error("expected: expression", token)
        return

    return Node(SUBTRACT, children=[left_hand_side, right_hand_side])

@rule(lexemes.PLUS_SIGN)
def parse_plus_sign(parser, previous_node):
    # Consume plus sign.
    token = parser.read_token()

    if not previous_node:
        parser.error("unexpected token: +", token)
        return

    left_hand_side  = previous_node
    right_hand_side = parser.parse_expression()

    if not right_hand_side:
        parser.error("expected: expression", token)
        return

    return Node(ADD, children=[left_hand_side, right_hand_side])

@rule(lexemes.SLASH)
def parse_slash(parser, previous_node):
    # Consume slash.
    token = parser.read_token()

    if not previous_node:
        parser.error("unexpected token: /", token)
        return

    left_hand_side  = previous_node
    right_hand_side = parser.parse_expression()

    if not right_hand_side:
        parser.error("expected: expression", token)
        return

    return Node(DIVIDE, children=[left_hand_side, right_hand_side])

@rule(lexemes.STRING)
def parse_string(parser, previous_node):
    token = parser.read_token()
    value = str(token.lexeme)

    if previous_node:
        parser.error("string was unexpected here", token)
        return

    if not value.startswith('"') or not value.endswith('"'):
        parser.error("unterminated string", token)
        return

    value = value[1:-1]

    return Node(STRING, value)
