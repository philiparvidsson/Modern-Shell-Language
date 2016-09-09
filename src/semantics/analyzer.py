#-------------------------------------------------
# IMPORTS
#-------------------------------------------------

from parsing.syntax import *
from semantics.scope import Scope

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

        self.scope = Scope()

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

    def enter_scope(self):
        self.scope = Scope(parent_scope=self.scope)

    def leave_scope(self):
        self.scope = self.scope.parent_scope

    @analyzes(ASSIGN, PASS_1)
    def __assign(self, node):
        if node.children[0].construct == IDENTIFIER:
            # FIXME: Keep type data?
            self.scope.decl_var(node.children[0].data, 'string')

    @analyzes(FUNC, PASS_1)
    def __func(self, node):
        self.scope.decl_var(node.data, 'string')

        self.enter_scope()

        decl = node.children[0]
        defi = node.children[1]

        print 'ass', decl
        for child in decl.children:
            print decl.construct

        self.leave_scope()


    @analyzes(IDENTIFIER, PASS_1)
    def __identifier(self, node):
        if not self.scope.is_decl(node.data):
            smaragd.error('identifier not declared: {}'.format(node.data), node.token)

    @analyzes(ADD, PASS_2)
    def __add(self, node):
        a = node.children[0]
        b = node.children[1]

        if (a.construct in (INTEGER, STRING)
        and b.construct in (INTEGER, STRING)
        and a.construct != b.construct):
            smaragd.warning('adding integer and string', node.token)

    @analyzes(DIVIDE, PASS_2)
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

    @analyzes(MULTIPLY, PASS_2)
    def __multiply(self, node):
        a = node.children[0]
        b = node.children[1]

        if (a.construct == STRING or b.construct == STRING):
            smaragd.error('multiplication only allowed with integers', node.token)

    @analyzes(SUBTRACT, PASS_2)
    def __subtract(self, node):
        a = node.children[0]
        b = node.children[1]

        if (a.construct == STRING or b.construct == STRING):
            smaragd.error('subtraction only allowed with integers', node.token)
