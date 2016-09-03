#--------------------------------------------------
# CONSTANTS
#--------------------------------------------------

ASTERISK          = 'asterisk'
COMMA             = 'comma'
END               = 'end'
EOF               = '<eof>'
EQUALS_SIGN       = 'equals sign'
FUNCTION          = 'function'
IDENTIFIER        = 'identifier'
INTEGER           = 'integer'
LEFT_PARENTHESIS  = 'left parenthesis'
MINUS_SIGN        = 'minus sign'
NEWLINE           = 'newline'
PLUS_SIGN         = 'plus sign'
RIGHT_PARENTHESIS = 'right parenthesis'
SLASH             = 'slash'
STRING            = 'string'

# FIXME: Order of iteration cannot be guaranteed.  How do we know lexer doesn't
# think func is an identifier?

LEXEMES = {
    '"[^"\n]*"?$'            : STRING,
    ','                      : COMMA,
    '-'                      : MINUS_SIGN,
    '-?[0-9]+'               : INTEGER,
    '/'                      : SLASH,
    '='                      : EQUALS_SIGN,
    '[_A-Za-z][_A-Za-z0-9]*' : IDENTIFIER,
    '\('                     : LEFT_PARENTHESIS,
    '\)'                     : RIGHT_PARENTHESIS,
    '\*'                     : ASTERISK,
    '\+'                     : PLUS_SIGN,
    'end'                    : END,
    'func'                   : FUNCTION,
}
