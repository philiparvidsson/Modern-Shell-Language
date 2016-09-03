#--------------------------------------------------
# IMPORTS
#--------------------------------------------------

class Node(object):
    def __init__(self, construct, data=None, children=None):
        self.children  = children
        self.construct = construct
        self.data      = data
