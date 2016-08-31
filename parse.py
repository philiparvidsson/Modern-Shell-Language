from crutch import Token

def into_tokens(source_code):
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
            token = Token(Token.EOL, "end-of-line")
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
            token = Token(Token.ASSIGNMENT, "=")

        # Colon
        elif char == ":":
            token = Token(Token.COLON, ":")

        # Identifiers.
        elif char.isalpha():
            value = ""
            while True:
                value += char
                char = source_code[0]
                if char != "" and not char.isalnum(): break
                column += 1
                source_code = source_code[1:]

            token = Token(Token.IDENTIFIER, value)

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

            token = Token(Token.STRING, value)

        # Numeral (10, 123, 1337 etc.)
        elif char.isdigit():
            value = ""
            while True:
                value += char
                char = source_code[0]
                if not char.isdigit(): break
                column += 1
                source_code = source_code[1:]

            token = Token(Token.NUMERAL, value)

        # Keywords.
        if token and token.kind == Token.IDENTIFIER:
            if token.value == "if": token.kind = Token.K_IF;


        if token:
            token.row = row
            token.column = column
            tokens += [token]

    tokens += [Token(Token.EOF, "end-of-file", row, column)]

    return tokens
