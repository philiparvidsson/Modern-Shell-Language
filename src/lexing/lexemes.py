#--------------------------------------------------
# CONSTANTS
#--------------------------------------------------

ASTERISK          = 'asterisk'
EOF               = '<eof>'
EQUALS_SIGN       = 'equals sign'
IDENTIFIER        = 'identifier'
INTEGER           = 'integer'
LEFT_PARENTHESIS  = 'left parenthesis'
NEWLINE           = 'newline'
PLUS_SIGN         = 'plus sign'
RIGHT_PARENTHESIS = 'right parenthesis'
STRING            = 'string'

LEXEMES = {
    '='                      : EQUALS_SIGN,
    '-?[0-9]+'               : INTEGER,
    '[_A-Za-z][_A-Za-z0-9]*' : IDENTIFIER,
    '\('                     : LEFT_PARENTHESIS,
    '\)'                     : RIGHT_PARENTHESIS,
    '\*'                     : ASTERISK,
    '\+'                     : PLUS_SIGN,
    '"[^"\n]*"?$'            : STRING,
}
