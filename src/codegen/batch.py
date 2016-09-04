#--------------------------------------------------
# IMPORTS
#--------------------------------------------------

from parsing import syntax

#--------------------------------------------------
# CLASSES
#--------------------------------------------------

class Batch(object):
    def __init__(self, ast):
        self.construct_map = {
            syntax.ADD        : self.__add,
            syntax.ASSIGNMENT : self.__assignment,
            syntax.FUNCTION   : self.__function,
            syntax.IDENTIFIER : self.__identifier,
            syntax.INTEGER    : self.__integer,
            syntax.PROGRAM    : self.__program,
        }

        self.ast = ast
        self.code = ''
        self.value_stack = []
        self.tempvar_counter = 0

    def emit(self, code):
        self.code += code + '\n'

    def generate_code(self, root=None):
        if not root:
            root = self.ast

        code_func = self.construct_map[root.construct]

        code_func(root)

        return self.code

    def tempvar_name(self):
        self.tempvar_counter += 1
        return '_{}'.format(self.tempvar_counter)

    def __add(self, node):
        lhs = node.children[0]
        rhs = node.children[1]

        self.generate_code(lhs)
        self.generate_code(rhs)

        temp = self.tempvar_name()
        self.emit('set /a {}={}+{}'.format(temp, self.value_stack.pop(), self.value_stack.pop()))
        self.value_stack.append('!{}!'.format(temp))

    def __assignment(self, node):
        switches = []

        ident = node.children[0]
        expr = node.children[1]

        self.generate_code(ident)
        self.generate_code(expr)

        if switches:
            self.emit('set {} {}={}'.format(' '.join(switches), identifier, 'loool'))
        else:
            self.emit('set {}={}'.format(ident.data, self.value_stack.pop()))


    def __function(self, node):
        self.emit(':{}'.format(node.data))

        self.emit('exit /b')

    def __identifier(self, node):
        self.value_stack.append('!{}!'.format(node.data))

    def __integer(self, node):
        self.value_stack.append(node.data)

    def __program(self, node):
        self.emit('setlocal enabledelayedexpansion')

        for child in node.children:
            self.generate_code(child)
