#--------------------------------------------------
# CONSTANTS
#--------------------------------------------------

# Special lexemes.
EOF = '<eof>'

# Special characters.
ASTERISK          = 'asterisk'
COMMA             = 'comma'
EQUALS_SIGN       = 'equals sign'
LEFT_PARENTHESIS  = 'left parenthesis'
MINUS_SIGN        = 'minus sign'
NEWLINE           = 'newline'
PLUS_SIGN         = 'plus sign'
RIGHT_PARENTHESIS = 'right parenthesis'
SLASH             = 'slash'

# Keywords.
END  = 'end'
FUNC = 'function'

# User specified.
IDENTIFIER = 'identifier'
INTEGER    = 'integer'
STRING     = 'string'

# Lexeme lookup table.
LEXEME_MAP = {
    # Special characters.
    ','  : COMMA,
    '-'  : MINUS_SIGN,
    '/'  : SLASH,
    '='  : EQUALS_SIGN,
    '\(' : LEFT_PARENTHESIS,
    '\)' : RIGHT_PARENTHESIS,
    '\*' : ASTERISK,
    '\+' : PLUS_SIGN,

    # Keywords.
    'end'  : END,
    'func' : FUNC,

    # User specified.

    '[_A-Za-z][_A-Za-z0-9]*' : IDENTIFIER,
    '[0-9]+'                 : INTEGER,
    '"[^"\n]*"?'             : STRING,
}
