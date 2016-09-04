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
            syntax.ASSIGNMENT : self.__generate_assignment,
            syntax.FUNCTION   : self.__generate_function,
            syntax.PROGRAM    : self.__generate_program,
        }

        self.ast = ast
        self.code = ''

    def emit(self, code):
        self.code += code + '\n'

    def generate_code(self, root=None):
        if not root:
            root = self.ast

        code_func = self.construct_map[root.construct]

        code_func(root)

        return self.code

    def __generate_assignment(self, node):
        self.emit('set lol=2')

    def __generate_function(self, node):
        self.emit(':{}'.format(node.data))

        self.emit('exit /b')

    def __generate_program(self, node):
        self.emit('setlocal enabledelayedexpansion')

        for child in node.children:
            self.generate_code(child)
