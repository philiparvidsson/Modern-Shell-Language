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

class ASTOptimizer(object):
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
            children = root.children
            root.children = []
            for child in children:
                node = self.optimize_ast(child)
                if node:
                    root.children.append(node)

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

    @node_optimizer(ASSIGN)
    def __assign(self, node):
        if hasattr(node, 'is_unused') and node.is_unused:
            return None

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

    @node_optimizer(FUNC)
    def __func(self, node):
        if hasattr(node, 'is_unused') and node.is_unused:
            return None

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
