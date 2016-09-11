#--------------------------------------------------
# IMPORTS
#--------------------------------------------------

import smaragd

from .node import Node

from lexing import lexemes

#--------------------------------------------------
# CONSTANTS
#--------------------------------------------------

ADD        = 'add'
ARRAY      = 'array'
ARRAY_IDX  = 'array index'
ASSIGN     = 'assign'
BIN_AND    = 'binary and'
BIN_OR     = 'binary or'
BIN_XOR    = 'binary xor'
DEC        = 'decrement'
DIVIDE     = 'divide'
ELSE       = 'else'
END        = 'end'
EQUAL      = 'equal'
FOR        = 'for'
FUNC       = 'func'
FUNC_CALL  = 'func call'
FUNC_DECL  = 'func decl'
FUNC_DEF   = 'func def'
GREATER    = 'greater'
GREATER_EQ = 'greater or eq'
IDENTIFIER = 'ident'
IF         = 'if'
IF_TERNARY = 'if ternary'
INC        = 'increment'
INTEGER    = 'integer'
LESS       = 'less'
LESS_EQ    = 'less or equal'
LOGIC_AND  = 'logic and'
LOGIC_OR   = 'logic or'
MODULO     = 'modulo'
MULTIPLY   = 'multiply'
NOOP       = 'no-op'
NOT_EQ     = 'not equal'
PROGRAM    = 'program'
RETURN     = 'return'
SHIFT_L    = 'left-shift'
SHIFT_R    = 'right-shift'
STRING     = 'string'
SUBTRACT   = 'subtract'
THEN       = 'then'
WHILE      = 'while'

#--------------------------------------------------
# FUNCTIONS
#--------------------------------------------------

def parse_expr(parser):
    parser.eat_whitespace()
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

    # <expr2> && <expr>
    elif tok.category == lexemes.LOGIC_AND:
        parser.read_token()
        expr = Node(LOGIC_AND, children=[expr, parse_expr(parser)])

    # <expr2> || <expr>
    elif tok.category == lexemes.LOGIC_OR:
        parser.read_token()
        expr = Node(LOGIC_OR, children=[expr, parse_expr(parser)])

    # <expr2> ? <expr> : <expr>
    elif tok.category == lexemes.Q_MARK:
        parser.read_token()
        parser.eat_whitespace()
        then_expr = parse_expr(parser)
        parser.eat_whitespace()
        parser.expect(lexemes.COLON)
        parser.eat_whitespace()
        else_expr = parse_expr(parser)
        expr = Node(IF_TERNARY, children=[expr, then_expr, else_expr])

    if expr:
        expr.token = tok

    return expr

def parse_expr2(parser):
    parser.eat_whitespace()
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

    # <expr3> == <expr>
    elif tok.category == lexemes.EQ_SIGN_2:
        parser.read_token()
        expr = Node(EQUAL, children=[expr, parse_expr3(parser)])

    # <expr3> != <expr>
    elif tok.category == lexemes.NOT_EQ:
        parser.read_token()
        expr = Node(NOT_EQ, children=[expr, parse_expr3(parser)])

    # <expr3> < <expr>
    elif tok.category == lexemes.LESS:
        parser.read_token()
        expr = Node(LESS, children=[expr, parse_expr3(parser)])

    # <expr3> > <expr>
    elif tok.category == lexemes.GREATER:
        parser.read_token()
        expr = Node(GREATER, children=[expr, parse_expr3(parser)])

    # <expr3> <= <expr>
    elif tok.category == lexemes.LESS_EQ:
        parser.read_token()
        expr = Node(LESS_EQ, children=[expr, parse_expr3(parser)])

    # <expr3> >= <expr>
    elif tok.category == lexemes.GREATER_EQ:
        parser.read_token()
        expr = Node(GREATER_EQ, children=[expr, parse_expr3(parser)])

    # <expr3>--
    elif tok.category == lexemes.MINUS_MINUS:
        parser.read_token()
        expr = Node(DEC, children=[expr])

    if expr:
        expr.token = tok

    return expr

def parse_expr3(parser):
    parser.eat_whitespace()
    expr = parse_expr4(parser)

    tok = parser.peek_token()

    # <expr3> (<expr>[, <expr> ...])
    if tok.category == lexemes.L_PAREN:
        while True:
            parser.expect(lexemes.L_PAREN)
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

            tok = parser.peek_token()
            if tok.category != lexemes.L_PAREN:
                break

    # <expr3>[<expr>]
    elif tok.category == lexemes.L_BRACK:
        while True:
            tok = parser.peek_token()
            if tok.category == lexemes.L_BRACK:
                parser.read_token()
                expr = Node(ARRAY_IDX, token=tok, children=[expr, parse_expr(parser)])
                parser.expect(lexemes.R_BRACK)
            elif tok.category == lexemes.PERIOD:
                parser.read_token()
                tok = parser.expect(lexemes.IDENT)
                expr = Node(ARRAY_IDX, token=tok, children=[expr, Node(STRING, tok.lexeme, tok)])
                tok = parser.peek_token()

            tok = parser.peek_token()
            if tok.category not in (lexemes.L_BRACK, lexemes.PERIOD):
                break

    if expr:
        expr.token = tok

    return expr

def parse_expr4(parser):
    parser.eat_whitespace()
    expr = None

    tok = parser.peek_token()

    # (<expr>)
    if tok.category == lexemes.L_PAREN:
        parser.expect(lexemes.L_PAREN)
        expr = parse_expr(parser)
        parser.expect(lexemes.R_PAREN)

    # [<expr>[, <expr> ...]]
    elif tok.category == lexemes.L_BRACK:
        parser.expect(lexemes.L_BRACK)

        items = []

        while True:
            tok = parser.peek_token()
            if tok.category == lexemes.R_BRACK:
                break

            parser.eat_whitespace()
            items.append(parse_expr(parser))
            parser.eat_whitespace()

            tok = parser.peek_token()
            if tok.category == lexemes.R_BRACK:
                break

            parser.expect(lexemes.COMMA)

        parser.eat_whitespace()
        parser.expect(lexemes.R_BRACK)

        expr = Node(ARRAY, token=tok, children=items)

    # <identifier>
    elif tok.category == lexemes.IDENT:
        expr = parse_ident(parser)

    # <integer>
    elif tok.category == lexemes.INT:
        expr = parse_int(parser)

    # <string>
    elif tok.category == lexemes.STR:
        expr = parse_str(parser)

    # for ([<expr>]; [<expr>]; [<expr>]) ...
    elif tok.category == lexemes.FOR:
        expr = parse_for(parser)

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

        if parser.peek_token().category == lexemes.NEWLINE:
            tok = parser.peek_token()
            smaragd.warning('prefer semicolon or expression on same row as return keyword', tok)

        parser.eat_whitespace()

        if parser.peek_token().category == lexemes.SEMICOLON:
            tok = parser.read_token()
            expr = Node(RETURN, children=[Node(INTEGER, 0, tok)])
        else:
            expr = Node(RETURN, children=[parse_expr(parser)])

    # true
    elif tok.category == lexemes.TRUE:
        parser.read_token()
        expr = Node(INTEGER, 1)

    # false
    elif tok.category == lexemes.FALSE:
        parser.read_token()
        expr = Node(INTEGER, 0)

    elif tok.category == lexemes.NOT:
        parser.read_token()
        parser.eat_whitespace()
        expr = parse_expr(parser)
        expr = Node(IF_TERNARY, children=[expr, Node(INTEGER, 0, tok), Node(INTEGER, 1, tok)])

    elif tok.category == lexemes.BREAK:
        parse.read_token()
        expr = Node(BREAK)

    elif tok.category == lexemes.CONTINUE:
        parse.read_token()
        expr = Node(CONTINUE)

    # <eof> | <newline>
    #elif tok.category in (lexemes.EOF, lexemes.NEWLINE):
    #    pass

    elif tok.category != lexemes.EOF:
        smaragd.error("unexpected token: {}".format(tok.category), tok)

    if expr:
        expr.token = tok

    return expr

def parse_for(parser):
    for_tok = parser.expect(lexemes.FOR, lexemes.L_PAREN)[0]

    init_expr = Node(NOOP)
    cond_expr = Node(NOOP)
    loop_expr = Node(NOOP)

    parser.eat_whitespace()

    tok = parser.peek_token()
    if tok.category != lexemes.SEMICOLON:
        init_expr = parse_expr(parser)

    parser.eat_whitespace()
    parser.expect(lexemes.SEMICOLON)

    tok = parser.peek_token()
    if tok.category != lexemes.SEMICOLON:
        cond_expr = parse_expr(parser)

    parser.eat_whitespace()
    parser.expect(lexemes.SEMICOLON)

    tok = parser.peek_token()
    if tok.category not in (lexemes.R_PAREN, lexemes.SEMICOLON):
        loop_expr = parse_expr(parser)

    parser.eat_whitespace()
    parser.expect(lexemes.R_PAREN)
    parser.eat_whitespace()

    node = Node(FOR, token=for_tok, children=[init_expr, cond_expr, loop_expr])

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

        parser.eat_whitespace()
        args.children.append(parse_ident(parser))

        tok = parser.peek_token()
        if tok.category == lexemes.R_PAREN:
            break

        parser.eat_whitespace()
        parser.expect(lexemes.COMMA)

    parser.expect(lexemes.R_PAREN)
    parser.eat_whitespace()
    parser.expect(lexemes.L_BRACE)
    parser.eat_whitespace()

    body = Node(FUNC_DEF, token=func_tok, children=[])

    while True:
        tok = parser.peek_token()
        if tok.category in (lexemes.EOF, lexemes.R_BRACE):
            break

        body.children.append(parse_expr(parser))
        parser.eat_whitespace(eat_semicolons=True)

    parser.eat_whitespace()
    parser.expect(lexemes.R_BRACE)

    return Node(FUNC, name, func_tok, [args, body])

def parse_ident(parser):
    tok = parser.expect(lexemes.IDENT)

    ident = Node(IDENTIFIER, tok.lexeme, tok)

    tok = parser.peek_token()
    if tok.category == lexemes.PERIOD:
        while True:
            parser.expect(lexemes.PERIOD)

            tok = parser.expect(lexemes.IDENT)
            ident = Node(ARRAY_IDX, token=tok, children=[ident, Node(STRING, tok.lexeme, tok)])

            tok = parser.peek_token()
            if tok.category != lexemes.PERIOD:
                break

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
        parser.eat_whitespace()

        while True:
            tok = parser.peek_token()
            if tok.category == lexemes.R_BRACE:
                parser.read_token()
                break

            then_expr.children.append(parse_expr(parser))
            parser.eat_whitespace(eat_semicolons=True)
    else:
        then_expr.children.append(parse_expr(parser))
        parser.eat_whitespace(eat_semicolons=True)

    parser.eat_whitespace()

    else_expr = Node(ELSE, token=tok, children=[])

    tok = parser.peek_token()
    if tok.category == lexemes.ELSE:
        parser.read_token()
        parser.eat_whitespace()

        tok = parser.peek_token()
        if tok.category == lexemes.L_BRACE:
            tok = parser.read_token()
            while True:
                parser.eat_whitespace()

                tok = parser.peek_token()
                if tok.category == lexemes.R_BRACE:
                    parser.read_token()
                    break

                else_expr.children.append(parse_expr(parser))
                parser.eat_whitespace(eat_semicolons=True)

        else:
            else_expr.children.append(parse_expr(parser))
            parser.eat_whitespace(eat_semicolons=True)


    return Node(IF, token=if_tok, children=[cond, then_expr, else_expr])

def parse_int(parser):
    tok = parser.expect(lexemes.INT)

    #if len(tok.lexeme) > 10:
    #    parser.warn("integer too large", tok)

    value = tok.lexeme
    if value.startswith("0x"):
        if len(value) == 2:
            smaragd.error("invalid hex value", tok)
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
            smaragd.error("unterminated string", tok)

    value = value[1:-1]

    return Node(STRING, value, tok)

def parse_while(parser):
    while_tok = parser.expect(lexemes.WHILE, lexemes.L_PAREN)[0]

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
