#--------------------------------------------------
# CLASSES
#--------------------------------------------------

class StringSource(object):
    def __init__(self, s):
        self.string = s

    def peek_char(self):
        if not self.string or len(self.string) == 0:
            return None

        return self.string[0]

    def read_char(self):
        if not self.string or len(self.string) == 0:
            return None

        char = self.string[0]

        # "Eat" the first character.
        self.string = self.string[1:]

        return char
