#-------------------------------------------------
# CONSTANTS
#-------------------------------------------------

AUTHORS = ["Philip Arvidsson <contact@philiparvidsson.com>"]
VERSION = "0.01"

#-------------------------------------------------
# CLASSES
#-------------------------------------------------

class Token(object):
    (UNKNOWN,
     ASSIGNMENT,
     COLON,
     EOF,
     EOL,
     IDENTIFIER,
     K_IF,
     NUMERAL,
     STRING) = range(9)

    def __init__(self, kind, value, row = 0, column = 0):
        self.row    = row
        self.column = column
        self.kind   = kind
        self.value  = value

    def __str__(self):
        return "Token(kind={}, row={}, column={}, value={})".format(self.kind, self.row, self.column, self.value)
