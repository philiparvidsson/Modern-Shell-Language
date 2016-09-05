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
ASSIGN     = 'assignment'
BIN_AND    = 'binary and'
BIN_OR     = 'binary or'
BIN_XOR    = 'binary xor'
DEC        = 'decrement'
DIVIDE     = 'divide'
ELSE       = 'else'
END        = 'end'
EQUAL      = 'equal'
FUNC       = 'function'
FUNC_CALL  = 'function call'
FUNC_DECL  = 'function declaration'
FUNC_DEF   = 'function definition'
GREATER    = 'greater than'
GREATER_EQ = 'greater than or equal'
IDENTIFIER = 'identifier'
IF         = 'if'
IF_TERNARY = 'if ternary'
INC        = 'increment'
INTEGER    = 'integer'
LESS       = 'less than'
LESS_EQ    = 'less than or equal'
LOGIC_AND  = 'logical and'
LOGIC_OR   = 'logic or'
MODULO     = 'modulo'
MULTIPLY   = 'multiply'
NOT_EQ     = 'not equal'
PROGRAM    = 'program'
RETURN     = 'return'
SHIFT_L    = 'shift left'
SHIFT_R    = 'shift right'
STRING     = 'string'
SUBTRACT   = 'subtract'
THEN       = 'then'
WHILE      = 'while'

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

    # <expr2> & <expr>
    elif tok.category == lexemes.BIN_AND:
        parser.read_token()
        expr = Node(BIN_AND, children=[expr, parse_expr(parser)])

    # <expr2> | <expr>
    elif tok.category == lexemes.BIN_OR:
        parser.read_token()
        expr = Node(BIN_OR, children=[expr, parse_expr(parser)])

    # <expr2> ^ <expr>
    elif tok.category == lexemes.BIN_XOR:
        parser.read_token()
        expr = Node(BIN_XOR, children=[expr, parse_expr(parser)])

    # <expr2> == <expr>
    elif tok.category == lexemes.EQ_SIGN_2:
        parser.read_token()
        expr = Node(EQUAL, children=[expr, parse_expr(parser)])

    # <expr2> != <expr>
    elif tok.category == lexemes.NOT_EQ:
        parser.read_token()
        expr = Node(NOT_EQUAL, children=[expr, parse_expr(parser)])

    # <expr2> < <expr>
    elif tok.category == lexemes.LESS:
        parser.read_token()
        expr = Node(LESS, children=[expr, parse_expr(parser)])

    # <expr2> > <expr>
    elif tok.category == lexemes.GREATER:
        parser.read_token()
        expr = Node(GREATER, children=[expr, parse_expr(parser)])

    # <expr2> <= <expr>
    elif tok.category == lexemes.LESS_EQ:
        parser.read_token()
        expr = Node(LESS_EQ, children=[expr, parse_expr(parser)])

    # <expr2> >= <expr>
    elif tok.category == lexemes.GREATER_EQ:
        parser.read_token()
        expr = Node(GREATER_EQ, children=[expr, parse_expr(parser)])

    # <expr2> && <expr>
    elif tok.category == lexemes.LOGIC_AND:
        parser.read_token()
        expr = Node(LOGIC_AND, children=[expr, parse_expr(parser)])

    # <expr2> || <expr>
    elif tok.category == lexemes.LOGIC_OR:
        parser.read_token()
        expr = Node(LOGIC_OR, children=[expr, parse_expr(parser)])

    if expr:
        expr.token = tok

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

    # <expr3> % <expr2>
    elif tok.category == lexemes.MODULO:
        parser.read_token()
        expr = Node(MODULO, children=[expr, parse_expr2(parser)])

    # <expr3> << <expr2>
    elif tok.category == lexemes.SHIFT_L:
        parser.read_token()
        expr = Node(SHIFT_L, children=[expr, parse_expr2(parser)])

    # <expr3> >> <expr2>
    elif tok.category == lexemes.SHIFT_R:
        parser.read_token()
        expr = Node(SHIFT_R, children=[expr, parse_expr2(parser)])

    # <expr3> += <expr2>
    elif tok.category == lexemes.PLUS_EQ:
        parser.read_token()
        expr = Node(ASSIGN, children=[
            expr,
            Node(ADD, children=[expr, parse_expr2(parser)])
        ])

    # <expr3> -= <expr2>
    elif tok.category == lexemes.MINUS_EQ:
        parser.read_token()
        expr = Node(ASSIGN, children=[
            expr,
            Node(SUBTRACT, children=[expr, parse_expr2(parser)])
        ])

    # <expr3> *= <expr2>
    elif tok.category == lexemes.ASTERISK_EQ:
        parser.read_token()
        expr = Node(ASSIGN, children=[
            expr,
            Node(MULTIPLY, children=[expr, parse_expr2(parser)])
        ])

    # <expr3> /= <expr2>
    elif tok.category == lexemes.SLASH_EQ:
        parser.read_token()
        expr = Node(ASSIGN, children=[
            expr,
            Node(DIVIDE, children=[expr, parse_expr2(parser)])
        ])

    # <expr3> %= <expr2>
    elif tok.category == lexemes.MODULO_EQ:
        parser.read_token()
        expr = Node(ASSIGN, children=[
            expr,
            Node(MODULO, children=[expr, parse_expr2(parser)])
        ])

    # <expr3> &= <expr2>
    elif tok.category == lexemes.BIN_AND_EQ:
        parser.read_token()
        expr = Node(ASSIGN, children=[
            expr,
            Node(BIN_AND, children=[expr, parse_expr2(parser)])
        ])

    # <expr3> |= <expr2>
    elif tok.category == lexemes.BIN_OR_EQ:
        parser.read_token()
        expr = Node(ASSIGN, children=[
            expr,
            Node(BIN_OR, children=[expr, parse_expr2(parser)])
        ])

    # <expr3> ^= <expr2>
    elif tok.category == lexemes.BIN_XOR_EQ:
        parser.read_token()
        expr = Node(ASSIGN, children=[
            expr,
            Node(BIN_XOR, children=[expr, parse_expr2(parser)])
        ])

    # <expr3> <<= <expr2>
    elif tok.category == lexemes.SHIFT_L_EQ:
        parser.read_token()
        expr = Node(ASSIGN, children=[
            expr,
            Node(SHIFT_L, children=[expr, parse_expr2(parser)])
        ])

    # <expr3> >>= <expr2>
    elif tok.category == lexemes.SHIFT_R_EQ:
        parser.read_token()
        expr = Node(ASSIGN, children=[
            expr,
            Node(SHIFT_R, children=[expr, parse_expr2(parser)])
        ])

    # <expr3>++
    elif tok.category == lexemes.PLUS_PLUS:
        parser.read_token()
        expr = Node(INC, children=[expr])

    # <expr3>--
    elif tok.category == lexemes.MINUS_MINUS:
        parser.read_token()
        expr = Node(DEC, children=[expr])

    # <expr3> ? <expr2> : <expr2>
    elif tok.category == lexemes.Q_MARK:
        parser.read_token()
        parser.eat_whitespace()
        then_expr = parse_expr2(parser)
        parser.eat_whitespace()
        parser.expect(lexemes.COLON)
        parser.eat_whitespace()
        else_expr = parse_expr2(parser)
        expr = Node(IF_TERNARY, children=[expr, then_expr, else_expr])

    if expr:
        expr.token = tok

    return expr

def parse_expr3(parser):
    expr = parse_expr4(parser)

    tok = parser.peek_token()

    # <expr4> (<expr>[, <expr> ...])
    if tok.category == lexemes.L_PAREN:
        parser.read_token()
        args = [expr]
        while True:
            tok = parser.peek_token()
            if tok.category == lexemes.R_PAREN:
                break

            args.append(parse_expr(parser))

            tok = parser.peek_token()
            if tok.category == lexemes.R_PAREN:
                break

            parser.expect(lexemes.COMMA)

        parser.expect(lexemes.R_PAREN)

        if len(args) == 0:
            args = None

        expr = Node(FUNC_CALL, token=tok, children=args)

    if expr:
        expr.token = tok

    return expr

def parse_expr4(parser):
    expr = None

    tok = parser.peek_token()

    # (<expr>)
    if tok.category == lexemes.L_PAREN:
        parser.expect(lexemes.L_PAREN)
        expr = parse_expr(parser)
        parser.expect(lexemes.R_PAREN)

    # <identifier>
    elif tok.category == lexemes.IDENT:
        expr = parse_ident(parser)

    # <integer>
    elif tok.category == lexemes.INT:
        expr = parse_int(parser)

    # <string>
    elif tok.category == lexemes.STR:
        expr = parse_str(parser)

    # func <identifier>(...)
    elif tok.category == lexemes.FUNC:
        expr = parse_func(parser)

    # if (<expr>) ...
    elif tok.category == lexemes.IF:
        expr = parse_if(parser)

    # while (<expr>) ...
    elif tok.category == lexemes.WHILE:
        expr = parse_while(parser)

    # return <expr>
    elif tok.category == lexemes.RETURN:
        parser.read_token()
        expr = Node(RETURN, token=tok, children=[parse_expr(parser)])

    # true
    elif tok.category == lexemes.TRUE:
        parser.read_token()
        expr = Node(INTEGER, 1)

    # false
    elif tok.category == lexemes.FALSE:
        parser.read_token()
        expr = Node(INTEGER, 0)

    # <eof> | <newline>
    #elif tok.category in (lexemes.EOF, lexemes.NEWLINE):
    #    pass

    elif tok.category != lexemes.EOF:
        parser.err("unexpected token: {}".format(tok.category), tok)

    if expr:
        expr.token = tok

    return expr

def parse_func(parser):
    func_tok = parser.expect(lexemes.FUNC)

    name = None

    # We have a name unless it's an anonymous function.
    if parser.peek_token().category == lexemes.IDENT:
        name = parse_ident(parser).data

    parser.expect(lexemes.L_PAREN)

    args = Node(FUNC_DECL, token=func_tok, children=[])

    while True:
        tok = parser.peek_token()
        if tok.category == lexemes.R_PAREN:
            break

        args.children.append(parse_ident(parser))

        tok = parser.peek_token()
        if tok.category == lexemes.R_PAREN:
            break

        parser.expect(lexemes.COMMA)

    parser.expect(lexemes.R_PAREN)
    parser.eat_whitespace()
    parser.expect(lexemes.L_BRACE)

    body = Node(FUNC_DEF, token=func_tok, children=[])

    while True:
        parser.eat_whitespace()

        tok = parser.peek_token()
        if tok.category in (lexemes.EOF, lexemes.R_BRACE):
            break

        body.children.append(parse_expr(parser))

    parser.expect(lexemes.R_BRACE)

    return Node(FUNC, name, func_tok, [args, body])

def parse_ident(parser):
    tok = parser.expect(lexemes.IDENT)

    ident = Node(IDENTIFIER, tok.lexeme, tok)

    tok = parser.peek_token()
    while tok.category == lexemes.PERIOD:
        parser.read_token()
        tok = parser.expect(lexemes.IDENT)

        ident = Node(IDENTIFIER, tok.lexeme, tok, children=[ident])

        tok = parser.peek_token()

    #if len(tok.lexeme) > 64:
    #    parser.warn("identifier unnecessarily long", tok)

    return ident

def parse_if(parser):
    if_tok = parser.expect(lexemes.IF, lexemes.L_PAREN)

    cond = parse_expr(parser)

    parser.expect(lexemes.R_PAREN)
    parser.eat_whitespace()

    then_expr = Node(THEN, token=if_tok, children=[])

    tok = parser.peek_token()
    if tok.category == lexemes.L_BRACE:
        parser.read_token()
        while True:
            parser.eat_whitespace()

            tok = parser.peek_token()
            if tok.category == lexemes.R_BRACE:
                parser.read_token()
                break

            then_expr.children.append(parse_expr(parser))
    else:
        then_expr.children.append(parse_expr(parser))

    parser.eat_whitespace()

    else_expr = Node(ELSE, token=tok, children=[])

    tok = parser.peek_token()
    if tok.category == lexemes.ELSE:
        parser.read_token()

        if tok.category == lexemes.L_BRACE:
            tok = parser.peek_token()
            while True:
                parser.eat_whitespace()

                tok = parser.peek_token()
                if tok.category == lexemes.R_BRACE:
                    parser.read_token()
                    break

                else_expr.children.append(parse_expr(parser))
        else:
            else_expr.children.append(parse_expr(parser))


    return Node(IF, token=if_tok, children=[cond, then_expr, else_expr])

def parse_int(parser):
    tok = parser.expect(lexemes.INT)

    #if len(tok.lexeme) > 10:
    #    parser.warn("integer too large", tok)

    value = tok.lexeme
    if value.startswith("0x"):
        if len(value) == 2:
            parser.err("invalid hex value", tok)
            value = 0
        else:
            value = int(value[2:], 16)
    elif value.endswith("b"):
        value = int(value[:-1], 2)

    return Node(INTEGER, int(value), tok)

def parse_str(parser):
    tok = parser.expect(lexemes.STR)

    value = str(tok.lexeme)

    if ((not value.startswith('"') or not value.endswith('"')) and
        (not value.startswith('\'') or not value.endswith('\''))):
            parser.err("unterminated string", tok)

    value = value[1:-1]

    return Node(STRING, value, tok)

def parse_while(parser):
    while_tok = parser.expect(lexemes.WHILE, lexemes.L_PAREN)

    cond = parse_expr(parser)

    parser.expect(lexemes.R_PAREN)
    parser.eat_whitespace()

    node = Node(WHILE, token=while_tok, children=[cond])

    tok = parser.peek_token()
    if tok.category == lexemes.L_BRACE:
        parser.read_token()
        while True:
            parser.eat_whitespace()

            tok = parser.peek_token()
            if tok.category == lexemes.R_BRACE:
                parser.read_token()
                break

            node.children.append(parse_expr(parser))
    else:
        node.children.append(parse_expr(parser))

    parser.eat_whitespace()

    return node
