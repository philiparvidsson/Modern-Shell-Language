#--------------------------------------------------
# CLASSES
#--------------------------------------------------

class Error(object):
    def __init__(self, message, row, column):
        self.message = message
        self.row     = row
        self.column = column

    def __str__(self):
        s = "lexing error @ {}:{}: {}"
        return s.format(self.row, self.column, self.message)
