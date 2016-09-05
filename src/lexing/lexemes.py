#--------------------------------------------------
# CONSTANTS
#--------------------------------------------------

# Special lexemes.
EOF = '<eof>'

# Special characters.
ASTERISK       = 'asterisk'
ASTERISK_EQ    = 'asterisk equals'
ASTERISK_SLASH = 'asterisk slash'
BIN_AND        = 'binary and'
BIN_AND_EQ     = 'binary and equals'
BIN_OR         = 'binary or'
BIN_OR_EQ      = 'binary or equals'
BIN_XOR        = 'binary xor'
BIN_XOR_EQ     = 'binary xor equals'
COLON          = 'colon'
COMMA          = 'comma'
EQ_SIGN        = 'equals sign'
EQ_SIGN_2      = 'double equals sign'
GREATER        = 'greater than'
GREATER_EQ     = 'greater than or equal'
LESS           = 'less than'
LESS_EQ        = 'less than or equal'
LOGIC_AND      = 'logical and'
LOGIC_OR       = 'logical or'
L_BRACE        = 'left brace'
L_PAREN        = 'left parenthesis'
MINUS_EQ       = 'minus equals'
MINUS_MINUS    = 'double minus sign'
MINUS_SIGN     = 'minus sign'
MODULO         = 'modulo'
MODULO_EQ      = 'modulo equals'
NEWLINE        = 'newline'
NOT_EQ         = 'not equal'
PERIOD         = 'period'
PLUS_EQ        = 'plus equals'
PLUS_PLUS      = 'double plus sign'
PLUS_SIGN      = 'plus sign'
Q_MARK         = 'question mark'
R_BRACE        = 'right brace'
R_PAREN        = 'right parenthesis'
SEMICOLON      = 'semicolon'
SHIFT_L        = 'shift left'
SHIFT_L_EQ     = 'shift left equals'
SHIFT_R        = 'shift right'
SHIFT_R_EQ     = 'shift right equals'
SLASH          = 'slash'
SLASH_2        = 'double slash'
SLASH_ASTERISK = 'slash asterisk'
SLASH_EQ       = 'slash equals'

# Keywords.
ELSE   = 'else'
FUNC   = 'function'
IF     = 'if'
WHILE  = 'while'
RETURN = 'return'
TRUE   = 'true'
FALSE  = 'false'

# User specified.
IDENT = 'identifier'
INT   = 'integer'
STR   = 'string'

# Lexeme lookup table.
LEXEME_MAP = {
    # Special characters.
    ','     : COMMA,
    '-'     : MINUS_SIGN,
    '/'     : SLASH,
    '//'    : SLASH_2,
    '/='    : SLASH_EQ,
    '/\*'   : SLASH_ASTERISK,
    '='     : EQ_SIGN,
    '=='    : EQ_SIGN_2,
    '\!='   : NOT_EQ,
    '\%'    : MODULO,
    '\%='   : MODULO_EQ,
    '\&'    : BIN_AND,
    '\&='   : BIN_AND_EQ,
    '\&\&'  : LOGIC_AND,
    '\('    : L_PAREN,
    '\)'    : R_PAREN,
    '\*'    : ASTERISK,
    '\*/'   : ASTERISK_SLASH,
    '\*='   : ASTERISK_EQ,
    '\+'    : PLUS_SIGN,
    '\+='   : PLUS_EQ,
    '\+\+'  : PLUS_PLUS,
    '\-='   : MINUS_EQ,
    '\-\-'  : MINUS_MINUS,
    '\.'    : PERIOD,
    '\:'    : COLON,
    '\;'    : SEMICOLON,
    '\<'    : LESS,
    '\<='   : LESS_EQ,
    '\<\<'  : SHIFT_L,
    '\<\<=' : SHIFT_L_EQ,
    '\>'    : GREATER,
    '\>='   : GREATER_EQ,
    '\>\>'  : SHIFT_R,
    '\>\>=' : SHIFT_R_EQ,
    '\?'    : Q_MARK,
    '\^'    : BIN_XOR,
    '\^='   : BIN_XOR_EQ,
    '\{'    : L_BRACE,
    '\|'    : BIN_OR,
    '\|='   : BIN_OR_EQ,
    '\|\|'  : LOGIC_OR,
    '\}'    : R_BRACE,

    # Keywords.
    'else'     : ELSE,
    'false'    : FALSE,
    'function' : FUNC,
    'if'       : IF,
    'return'   : RETURN,
    'true'     : TRUE,
    'while'    : WHILE,

    # User specified.
    '0x[0-9A-Fa-f]*'         : INT,
    '[0-1]+b'                : INT,
    '[0-9]+'                 : INT,
    '"[^"\n]*"?'             : STR,
    '\'[^\'\n]*\'?'          : STR,
    '[_A-Za-z][_A-Za-z0-9]*' : IDENT,
}
