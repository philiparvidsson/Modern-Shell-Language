#--------------------------------------------------
# CONSTANTS
#--------------------------------------------------

EQUALS_SIGN = 'equals sign'
IDENTIFIER  = 'identifier'
INTEGER     = 'integer'
STRING      = 'string'

LEXEMES = {
    '='                      : EQUALS_SIGN,
    '[_A-Za-z][_A-Za-z0-9]*' : IDENTIFIER,
    '[0-9]+'                 : INTEGER,
    '".*"?'                  : STRING
}
