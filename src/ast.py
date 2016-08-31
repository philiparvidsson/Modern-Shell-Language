#-------------------------------------------------
# IMPORTS
#-------------------------------------------------

import ast

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
