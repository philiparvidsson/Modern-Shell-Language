#-------------------------------------------------
# CONSTANTS
#-------------------------------------------------

AUTHORS = ["Philip Arvidsson <contact@philiparvidsson.com>"]
VERSION = "0.01"

#-------------------------------------------------
# CLASSES
#-------------------------------------------------

class StringEater(object):
    def __init__(self, string):
        self.string = string

    def peek_char(self, num_chars_to_skip = 0):
        return self.string[num_chars_to_skip]

    def get_char(self):
        char = self.string[0]
        self.string = self.string[1:]
        return char

    def get_chars(self, num_chars):
        chars = self.string[:num_chars]
        self.string = self.string[num_chars:]
        return chars

    def num_chars_left(self):
        return len(self.string)

#-------------------------------------------------
# FUNCTIONS
#-------------------------------------------------
