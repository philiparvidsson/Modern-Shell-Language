#--------------------------------------------------
# CONSTANTS
#--------------------------------------------------

# Special lexemes.
EOF = '<eof>'

# Special characters.
ASTERISK   = 'asterisk'
COMMA      = 'comma'
EQ_SIGN    = 'equals sign'
EQ_SIGN_2  = 'double equals sign'
L_BRACE    = 'left brace'
L_PAREN    = 'left parenthesis'
MINUS_SIGN = 'minus sign'
NEWLINE    = 'newline'
PLUS_SIGN  = 'plus sign'
R_BRACE    = 'right brace'
R_PAREN    = 'right parenthesis'
RETURN     = 'return'
SEMICOLON  = 'semicolon'
SLASH      = 'slash'
SLASH_2    = 'double slash'

# Keywords.
ELSE = 'else'
FUNC = 'function'
IF   = 'if'

# User specified.
IDENT = 'identifier'
INT   = 'integer'
STR   = 'string'

# Lexeme lookup table.
LEXEME_MAP = {
    # Special characters.
    ','  : COMMA,
    '-'  : MINUS_SIGN,
    '/'  : SLASH,
    '//' : SLASH_2,
    '='  : EQ_SIGN,
    '==' : EQ_SIGN_2,
    '\(' : L_PAREN,
    '\)' : R_PAREN,
    '\*' : ASTERISK,
    '\+' : PLUS_SIGN,
    '\;' : SEMICOLON,
    '\{' : L_BRACE,
    '\}' : R_BRACE,

    # Keywords.
    'else'     : ELSE,
    'function' : FUNC,
    'if'       : IF,
    'return'   : RETURN,

    # User specified.
    '"[^"\n]*"?'             : STR,
    '[0-9]+'                 : INT,
    '[_A-Za-z][_A-Za-z0-9]*' : IDENT,
}
