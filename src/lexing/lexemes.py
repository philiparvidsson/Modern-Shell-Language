#--------------------------------------------------
# CONSTANTS
#--------------------------------------------------

# Special lexemes.
EOF = '<eof>'

# Special characters.
ASTERISK    = 'asterisk'
ASTERISK_EQ = 'asterisk equals'
COMMA       = 'comma'
EQ_SIGN     = 'equals sign'
EQ_SIGN_2   = 'double equals sign'
GREATER     = 'greater than'
GREATER_EQ  = 'greater than or equal'
LESS        = 'less than'
LESS_EQ     = 'less than or equal'
L_BRACE     = 'left brace'
L_PAREN     = 'left parenthesis'
MINUS_EQ    = 'minus equals'
MINUS_MINUS = 'double minus sign'
MINUS_SIGN  = 'minus sign'
NEWLINE     = 'newline'
NOT_EQ      = 'not equal'
PLUS_EQ     = 'plus equals'
PLUS_PLUS   = 'double plus sign'
PLUS_SIGN   = 'plus sign'
R_BRACE     = 'right brace'
R_PAREN     = 'right parenthesis'
SEMICOLON   = 'semicolon'
SLASH       = 'slash'
SLASH_2     = 'double slash'
SLASH_EQ    = 'slash equals'

# Keywords.
ELSE   = 'else'
FUNC   = 'function'
IF     = 'if'
WHILE  = 'while'
RETURN = 'return'

# User specified.
IDENT = 'identifier'
INT   = 'integer'
STR   = 'string'

# Lexeme lookup table.
LEXEME_MAP = {
    # Special characters.
    ','    : COMMA,
    '-'    : MINUS_SIGN,
    '/'    : SLASH,
    '//'   : SLASH_2,
    '/='   : SLASH_EQ,
    '='    : EQ_SIGN,
    '=='   : EQ_SIGN_2,
    '\!='  : NOT_EQ,
    '\('   : L_PAREN,
    '\)'   : R_PAREN,
    '\*'   : ASTERISK,
    '\*='  : ASTERISK_EQ,
    '\+'   : PLUS_SIGN,
    '\+='  : PLUS_EQ,
    '\+\+' : PLUS_PLUS,
    '\-='  : MINUS_EQ,
    '\-\-' : MINUS_MINUS,
    '\;'   : SEMICOLON,
    '\<'   : LESS,
    '\<='  : LESS_EQ,
    '\>'   : GREATER,
    '\>='  : GREATER_EQ,
    '\{'   : L_BRACE,
    '\}'   : R_BRACE,

    # Keywords.
    'else'     : ELSE,
    'function' : FUNC,
    'if'       : IF,
    'return'   : RETURN,
    'while'    : WHILE,

    # User specified.
    '"[^"\n]*"?'             : STR,
    '[0-9]+'                 : INT,
    '[_A-Za-z][_A-Za-z0-9]*' : IDENT,
}
