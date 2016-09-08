#-------------------------------------------------
# IMPORTS
#-------------------------------------------------

from parsing.syntax import *

#-------------------------------------------------
# CLASSES
#-------------------------------------------------

def node_optimizer(construct):
    def decorator(func):
        func._no_construct = construct
        return func

    return decorator

class Optimizer(object):
    def __init__(self):
        self.optimize_constants = True
        self.optimize_literals  = True

        self.optimizer_funcs = dict()

        for s in dir(self):
            func = getattr(self, s, None)
            if not hasattr(func, '_no_construct'):
                continue

            self.optimizer_funcs[func._no_construct] = func

    def optimize_ast(self, root):
        if root.children:
            num_children = len(root.children)
            for i in range(num_children):
                root.children[i] = self.optimize_ast(root.children[i])

        if root.construct in self.optimizer_funcs:
            func = self.optimizer_funcs[root.construct]
            return func(root)

        return root

    @node_optimizer(ADD)
    def __add(self, node):
        if not self.optimize_literals:
            return node

        a = node.children[0]
        b = node.children[1]

        if a.construct == INTEGER and b.construct == INTEGER:
            value = int(a.data) + int(b.data)
            return Node(INTEGER, value, node.token)

        if a.construct in (INTEGER, STRING) and b.construct in (INTEGER, STRING):
            value = str(a.data) + str(b.data)
            return Node(STRING, value, node.token)

        return node

    @node_optimizer(DIVIDE)
    def __divide(self, node):
        if not self.optimize_literals:
            return node

        a = node.children[0]
        b = node.children[1]

        if a.construct == INTEGER and b.construct == INTEGER:
            value = int(a.data) / int(b.data)
            return Node(INTEGER, value, node.token)

        return node

    @node_optimizer(MULTIPLY)
    def __multiply(self, node):
        if not self.optimize_literals:
            return node

        a = node.children[0]
        b = node.children[1]

        if a.construct == INTEGER and b.construct == INTEGER:
            value = int(a.data) * int(b.data)
            return Node(INTEGER, value, node.token)

        return node

    @node_optimizer(SUBTRACT)
    def __subtract(self, node):
        if not self.optimize_literals:
            return node

        a = node.children[0]
        b = node.children[1]

        if a.construct == INTEGER and b.construct == INTEGER:
            value = int(a.data) - int(b.data)
            return Node(INTEGER, value, node.token)

        return node
