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
    def __init__(self):
        self.analyzer_funcs = {}

        for s in dir(self):
            func = getattr(self, s, None)
            if not hasattr(func, '_na_construct'):
                continue

            p = func._na_pass
            c = func._na_construct

            if p not in self.analyzer_funcs:
                self.analyzer_funcs[p] = {}

            self.analyzer_funcs[p][c] = func

    def verify(self, ast):
        for p in range(1, 5):
            self.verify_internal(ast, p)

    def verify_internal(self, node, p):
        if p in self.analyzer_funcs:
            funcs = self.analyzer_funcs[p]
            if node.construct in funcs:
                funcs[node.construct](node)

        if node.children:
            for child in node.children:
                self.verify_internal(child, p)

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

        if (a.construct == STRING or b.construct == STRING):
                smaragd.error('division only allowed with integers', node.token)

        elif (a.construct == INTEGER and b.construct == INTEGER):
            if int(a.data) < int(b.data):
                smaragd.warning('division will result in zero', node.token)
            elif int(b.data) == 0:
                smaragd.warning('division by zero', node.token)

    @analyzes(MULTIPLY, PASS_1)
    def __multiply(self, node):
        a = node.children[0]
        b = node.children[1]

        if (a.construct == STRING or b.construct == STRING):
                smaragd.error('multiplication only allowed with integers', node.token)

    @analyzes(SUBTRACT, PASS_1)
    def __subtract(self, node):
        a = node.children[0]
        b = node.children[1]

        if (a.construct == STRING or b.construct == STRING):
                smaragd.error('subtraction only allowed with integers', node.token)
