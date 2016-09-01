#-------------------------------------------------
# IMPORTS
#-------------------------------------------------

from . import core

#-------------------------------------------------
# CLASSES
#-------------------------------------------------

class Node(object):
    def __init__(self, kind, value = "", children = []):
        self.parent   = None
        self.children = children

        self.kind  = kind
        self.value = value

    def __str__(self):
        children = []
        for child in self.children:
            children += [str(child)]
        return "Node(value={}, children={})".format(self.value, children)
