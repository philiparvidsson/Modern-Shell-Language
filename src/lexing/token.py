#--------------------------------------------------
# CLASSES
#--------------------------------------------------

class Token(object):
    def __init__(self, category, lexeme=None, row=None, column=None):
        self.category = category
        self.lexeme   = lexeme

        self.row    = row
        self.column = column

    def __str__(self):
        # FIXME: Shouldn't display lexeme if it is none
        s = '{}(category=\'{}\', lexeme=\'{}\', row={}, column={})'

        return s.format(
            type(self).__name__,
            self.category,
            self.lexeme,
            self.row,
            self.column)
