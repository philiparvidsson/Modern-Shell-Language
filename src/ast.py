#-------------------------------------------------
# CLASSES
#-------------------------------------------------

class Node(object):
    (ASSIGN, NUMERAL, VARIABLE) = range(3)

    def __init__(self):
        self.parent   = None
        self.children = []

        self.kind  = None
        self.value = None

#-------------------------------------------------
# FUNCTIONS
#-------------------------------------------------

def expression(tokens):
    token = tokens[0]

    return None

def from_tokens(tokens):
    root = expression(tokens)

    return root
