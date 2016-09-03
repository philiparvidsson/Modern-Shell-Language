#--------------------------------------------------
# IMPORTS
#--------------------------------------------------

import re

from .error   import Error
from .lexemes import LEXEMES
from .token   import Token

#--------------------------------------------------
# CLASSES
#--------------------------------------------------

class Lexer(object):
    def __init__(self, source):
        self.row    = 1
        self.column = 1

        self.source = source

    def create_token(self, lexeme):
        # Find the longest possible matching lexeme.
        for regex, category in LEXEMES.iteritems():
            match = re.match(regex, lexeme)
            if not match or match.group() != lexeme:
                continue

            # Our lexeme matches the regex so we can create a token.
            return Token(category, lexeme)

        # No match found.
        return None

    def peek_token(self):
        print "not implemented yet"
        assert False
        pass

    def read_token(self):
        # Skip whitespace.
        char = self.peek_char()
        while char and char.isspace():
            self.read_char()
            char = self.peek_char()

        lexeme = ''
        row    = self.row
        column = self.column

        token = None
        while True:
            char = self.peek_char()

            # Maybe we have reached the end of the source?
            if not char:
                break

            lexeme += char

            # Attempt to create a token from the lexeme.
            temp = self.create_token(lexeme)
            if not temp:
                break

            token = temp

            # Consume the character that made the token creation possible.
            self.read_char()

        if token:
            token.row = row
            token.column = column
            return token

        if len(lexeme) == 0:
            # We've reached the end of the source.
            return None

        s = "sequence not understood: {}"
        return Error(s.format(lexeme), row, column)

    def peek_char(self):
        return self.source.peek_char()

    def read_char(self):
        char = self.source.read_char()

        # Skip carriage returns entirely.
        while char == '\r':
            char = self.source.read_char()

        if char == '\n':
            self.column = 1
            self.row += 1
        elif char == '\t':
            # Assume tab width is eight characters.
            self.column += 8
        else:
            self.column += 1

        return char
