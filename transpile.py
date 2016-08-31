from enum import Enum

class Token(object):
    (unknown,
     assignment,
     colon,
     eof,
     eol,
     identifier,
     k_if,
     numeral,
     string) = range(9)

    def __init__(self, kind, value, row = 0, column = 0):
        self.row    = row
        self.column = column
        self.kind   = kind
        self.value  = value

    def __str__(self):
        return "Token(kind={}, row={}, column={}, value={})".format(self.kind, self.row, self.column, self.value)

def parse_into_tokens(source_code):
    tokens = []

    row    = 1
    column = 1

    while len(source_code) > 0:
        # TODO: Replace all these duplicate lines with some function call.
        char = source_code[0]
        source_code = source_code[1:]
        token = None

        # Line breaks etc.
        if char == "\n":
            token = Token(Token.eol, "end-of-line")
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
            token = Token(Token.assignment, "=")

        # Colon
        elif char == ":":
            token = Token(Token.colon, ":")

        # Identifiers.
        elif char.isalpha():
            value = ""
            while True:
                value += char
                char = source_code[0]
                if char != "" and not char.isalnum(): break
                column += 1
                source_code = source_code[1:]

            token = Token(Token.identifier, value)

        # String literals.
        elif char == "\"":
            value = ""
            char = source_code[0]
            source_code = source_code[1:]
            while True:
                value += char
                char = source_code[0]
                # FIX: Escaped double quote should nod terminate literal.
                column += 1
                source_code = source_code[1:]
                if char == "\"": break

            token = Token(Token.string, value)

        # Numeral (10, 123, 1337 etc.)
        elif char.isdigit():
            value = ""
            while True:
                value += char
                char = source_code[0]
                if not char.isdigit(): break
                column += 1
                source_code = source_code[1:]

            token = Token(Token.numeral, value)

        # Keywords.
        if token and token.kind == Token.identifier:
            if token.value == "if": token.kind = Token.k_if;


        if token:
            token.row = row
            token.column = column
            tokens += [token]

    tokens += [Token(Token.eof, "end-of-file", row, column)]

    return tokens

def transpile(file_name):
    file = open(file_name);
    source_code = file.read()
    file.close()

    tokens = parse_into_tokens(source_code)

    for token in tokens:
        print str(token)

if __name__=="__main__":
    transpile("test.mb")
