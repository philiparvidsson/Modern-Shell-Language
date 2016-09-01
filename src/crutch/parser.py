#-------------------------------------------------
# IMPORTS
#-------------------------------------------------

from . import core

#-------------------------------------------------
# CONSTANTS
#-------------------------------------------------

# Below are the token types.
ASSIGNMENT  = "="
COLON       = ":"
END_OF_FILE = "<eof>"
IDENTIFIER  = "identifier"
IF          = "if"
NEWLINE     = "\\n"
NUMERAL     = "numeral"
STRING      = "string"
UNKNOWN     = "<unknown>"

#-------------------------------------------------
# CLASSES
#-------------------------------------------------

class Token(object):
    def __init__(self, kind, value = None, row = 0, column = 0):
        self.row    = row
        self.column = column

        self.kind  = kind
        self.value = value

    def __str__(self):
        return "Token(kind={}, row={}, column={}, value={})".format(self.kind, self.row, self.column, self.value)

#-------------------------------------------------
# FUNCTIONS
#-------------------------------------------------

def parse_into_tokens(source_code):
    tokens = []

    row    = 1
    column = 1

    source_code = core.StringEater(source_code)

    while source_code.num_chars_left() > 0:
        char = source_code.get_char()
        token = None

        # Line breaks etc.
        if char == "\n":
            token = Token(NEWLINE)
            row += 1
            column = 1
        elif char == "\r":
            pass

        # Whitespace.
        elif char == " ":
            column += 1
        elif char == "\t":
            # Assume tab width is eight characters.
            column += 8

        # Assignment (identifier = expression)
        elif char == "=":
            column += 1
            token = Token(ASSIGNMENT, "=")

        # Colon
        elif char == ":":
            column += 1
            token = Token(COLON, ":")

        # Identifiers.
        elif char.isalpha():
            value = ""
            while True:
                value += char
                char = source_code.peek_char()
                if char != "" and not char.isalnum(): break
                column += 1
                source_code.get_char()

            token = Token(IDENTIFIER, value)

        # String literals.
        elif char == "\"":
            value = ""
            char = source_code.get_char()
            while True:
                value += char
                char = source_code.get_char()
                # FIXME: Escaped double quote should nod terminate literal.
                column += 1
                if char == "\"": break

            token = Token(STRING, value)

        # Numeral (10, 123, 1337 etc.)
        elif char.isdigit():
            value = ""
            while True:
                value += char
                char = source_code.peek_char()
                if not char.isdigit(): break
                column += 1
                source_code.get_char()

            token = Token(NUMERAL, value)

        # Keywords.
        if token and token.kind == IDENTIFIER:
            if token.value == "if": token.kind = Token.K_IF;

        if token:
            token.row    = row
            token.column = column

            tokens.append(token)

    tokens.append(Token(END_OF_FILE, None, row, column))

    return tokens
