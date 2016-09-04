#--------------------------------------------------
# IMPORTS
#--------------------------------------------------

import copy

from .node import Node

from lexing import lexemes

#--------------------------------------------------
# CONSTANTS
#--------------------------------------------------

ADD          = 'add'
ASSIGN       = 'assignment'
DIVIDE       = 'divide'
END          = 'end'
FUNC         = 'function'
FUNC_CALL    = 'function call'
FUNC_DECL    = 'function declaration'
FUNC_DEF     = 'function definition'
IDENTIFIER   = 'identifier'
INTEGER      = 'integer'
MULTIPLY     = 'multiply'
PROGRAM      = 'program'
STRING       = 'string'
SUBTRACT     = 'subtract'

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

def parse_expr(parser):
    expr = parse_expr2(parser)

    tok = parser.peek_token()

    # <expr2> = <expr>
    if tok.category == lexemes.EQ_SIGN:
        parser.read_token()
        expr = Node(ASSIGN, children=[expr, parse_expr(parser)])

    # <expr2> + <expr>
    if tok.category == lexemes.PLUS_SIGN:
        parser.read_token()
        expr = Node(ADD, children=[expr, parse_expr(parser)])

    # <expr2> - <expr>
    elif tok.category == lexemes.MINUS_SIGN:
        parser.read_token()
        expr = Node(SUBTRACT, children=[expr, parse_expr(parser)])

    return expr

def parse_expr2(parser):
    expr = parse_expr3(parser)

    tok = parser.peek_token()

    # <expr3> * <expr2>
    if tok.category == lexemes.ASTERISK:
        parser.read_token()
        expr = Node(MULTIPLY, children=[expr, parse_expr2(parser)])

    # <expr3> / <expr2>
    elif tok.category == lexemes.SLASH:
        parser.read_token()
        expr = Node(DIVIDE, children=[expr, parse_expr2(parser)])

    return expr

def parse_expr3(parser):
    expr = parse_expr4(parser)

    tok = parser.peek_token()

    # <expr4> (<expr>[, <expr> ...])
    if tok.category == lexemes.LEFT_PAREN:
        parser.read_token()
        args = []
        while True:
            tok = parser.peek_token()
            if tok.category == lexemes.RIGHT_PAREN:
                break

            args.append(parse_expr(parser))

            tok = parser.peek_token()
            if tok.category == lexemes.RIGHT_PAREN:
                break

            parser.expect(lexemes.COMMA)

        parser.expect(lexemes.RIGHT_PAREN)

        if len(args) == 0:
            args = None

        expr = Node(FUNC_CALL, expr.data, args)

    return expr

def parse_expr4(parser):
    expr = None

    tok = parser.peek_token()

    # (<expr>)
    if tok.category == lexemes.LEFT_PAREN:
        parser.expect(lexemes.LEFT_PAREN)
        expr = parse_expr(parser)
        parser.expect(lexemes.RIGHT_PAREN)

    # <identifier>
    elif tok.category == lexemes.IDENT:
        expr = parse_ident(parser)

    # <integer>
    elif tok.category == lexemes.INT:
        expr = parse_int(parser)

    # <string>
    elif tok.category == lexemes.STR:
        expr = parse_str(parser)

    # func <identifier>()
    elif tok.category == lexemes.FUNC:
        expr = parse_func(parser)

    # <eof> | <newline>
    #elif tok.category in (lexemes.EOF, lexemes.NEWLINE):
    #    pass

    else:
        parser.err("unexpected token: {}".format(tok.category), tok)

    return expr

def parse_func(parser):
    parser.expect(lexemes.FUNC)

    name = parse_ident(parser).data

    parser.expect(lexemes.LEFT_PAREN)

    args = Node(FUNC_DECL, children=[])

    while True:
        tok = parser.peek_token()
        if tok.category == lexemes.RIGHT_PAREN:
            break

        args.children.append(parse_ident(parser))

        tok = parser.peek_token()
        if tok.category == lexemes.RIGHT_PAREN:
            break

        parser.expect(lexemes.COMMA)

    parser.expect(lexemes.RIGHT_PAREN)

    body = Node(FUNC_DEF, children=[])

    while True:
        tok = parser.peek_token()
        while tok.category == lexemes.NEWLINE:
            parser.read_token()
            tok = parser.peek_token()

        if tok.category in (lexemes.END, lexemes.EOF):
            break

        body.children.append(parse_expr(parser))

    parser.expect(lexemes.END)

    return Node(FUNC, name, [args, body])

def parse_ident(parser):
    tok = parser.expect(lexemes.IDENT)

    #if len(tok.lexeme) > 64:
    #    parser.warn("identifier unnecessarily long", tok)

    return Node(IDENTIFIER, tok.lexeme)

def parse_int(parser):
    tok = parser.expect(lexemes.INT)

    #if len(tok.lexeme) > 10:
    #    parser.warn("integer too large", tok)

    return Node(INTEGER, int(tok.lexeme))

def parse_str(parser):
    tok = parser.expect(lexemes.STR)

    value = str(tok.lexeme)

    if not value.startswith('"') or not value.endswith('"'):
        parser.error("unterminated string", token)

    value = value[1:-1]

    return Node(STRING, value)
