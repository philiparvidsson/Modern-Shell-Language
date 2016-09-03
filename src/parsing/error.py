#--------------------------------------------------
# CLASSES
#--------------------------------------------------

class Error(object):
    def __init__(self, message, token):
        self.message = message
        self.token   = token

    def __str__(self):
        s = "parsing error @ {}:{}: {}"
        return s.format(self.token.row, self.token.column, self.message)
