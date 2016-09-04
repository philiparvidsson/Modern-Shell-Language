#--------------------------------------------------
# CONSTANTS
#--------------------------------------------------

# Special lexemes.
EOF = '<eof>'

# Special characters.
ASTERISK    = 'asterisk'
COMMA       = 'comma'
EQ_SIGN     = 'equals sign'
LEFT_PAREN  = 'left parenthesis'
MINUS_SIGN  = 'minus sign'
NEWLINE     = 'newline'
PLUS_SIGN   = 'plus sign'
RIGHT_PAREN = 'right parenthesis'
SLASH       = 'slash'

# Keywords.
END  = 'end'
FUNC = 'function'

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
    '\(' : LEFT_PAREN,
    '\)' : RIGHT_PAREN,
    '\*' : ASTERISK,
    '\+' : PLUS_SIGN,

    # Keywords.
    'end'  : END,
    'func' : FUNC,

    # User specified.

    '[_A-Za-z][_A-Za-z0-9]*' : IDENT,
    '[0-9]+'                 : INT,
    '"[^"\n]*"?'             : STR,
}
