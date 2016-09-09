#-------------------------------------------------
# IMPORTS
#-------------------------------------------------

from parsing.syntax import *

#-------------------------------------------------
# CONSTANTS
#-------------------------------------------------

PASS_1 = 1
PASS_2 = 2
PASS_3 = 3
PASS_4 = 4

#-------------------------------------------------
# CLASSES
#-------------------------------------------------

def analyzes(c, p):
    def decorator(func):
        func._na_pass      = p
        func._na_construct = c

        return func

    return decorator

class SemanticAnalyzer(object):
    def __init__():
        pass

    def analyze(ast):
        pass

    @analyzes(ADD, PASS_1)
    def __add(self, node):
        a = node.children[0]
        b = node.children[1]

        if (a.construct in (INTEGER, STRING)
        and b.construct in (INTEGER, STRING)
        and a.construct != b.construct):
            smaragd.warning('adding integer and string', node.token)

    @analyzes(DIVIDE, PASS_1)
    def __divide(self, node):
        a = node.children[0]
        b = node.children[1]

        if (a.construct in (INTEGER, STRING)
        and b.construct in (INTEGER, STRING)
        and a.construct != b.construct):
            smaragd.warning('dividing integer and string', node.token)


    @analyzes(MULTIPLY, PASS_1)
    def __divide(self, node):
        a = node.children[0]
        b = node.children[1]

        if (a.construct in (INTEGER, STRING)
        and b.construct in (INTEGER, STRING)
        and a.construct != b.construct):
            smaragd.warning('multiplying integer and string', node.token)

    @analyzes(SUBTRACT, PASS_1)
    def __subtract(self, node):
        a = node.children[0]
        b = node.children[1]

        if (a.construct in (INTEGER, STRING)
        and b.construct in (INTEGER, STRING)
        and a.construct != b.construct):
            smaragd.warning('subtracting integer and string', node.token)
