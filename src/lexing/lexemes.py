#--------------------------------------------------
# CONSTANTS
#--------------------------------------------------

COMMENT_CHAR = '#'

# Special lexemes.
EOF = '<eof>'

# Special characters.
ASTERISK       = 'asterisk'
COMMA          = 'comma'
DOUBLE_EQ_SIGN = 'double equals sign'
EQ_SIGN        = 'equals sign'
LEFT_PAREN     = 'left parenthesis'
MINUS_SIGN     = 'minus sign'
NEWLINE        = 'newline'
PLUS_SIGN      = 'plus sign'
RIGHT_PAREN    = 'right parenthesis'
SLASH          = 'slash'

# Keywords.
ELSE = 'else'
END  = 'end'
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
    '='  : EQ_SIGN,
    '==' : DOUBLE_EQ_SIGN,
    '\(' : LEFT_PAREN,
    '\)' : RIGHT_PAREN,
    '\*' : ASTERISK,
    '\+' : PLUS_SIGN,

    # Keywords.
    'else' : ELSE,
    'end'  : END,
    'func' : FUNC,
    'if'   : IF,

    # User specified.

    '[_A-Za-z][_A-Za-z0-9]*' : IDENT,
    '[0-9]+'                 : INT,
    '"[^"\n]*"?'             : STR,
}
