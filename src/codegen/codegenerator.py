#--------------------------------------------------
# IMPORTS
#--------------------------------------------------

from parsing.syntax import FUNC_CALL

#--------------------------------------------------
# CLASSES
#--------------------------------------------------

class CodeGenerator(object):
    def __init__(self, ast):
        self.ast = ast
        self.code = ''
        self.code_funcs = dict()

        for s in dir(self):
            func = getattr(self, s, None)
            if not hasattr(func, '_cg_construct'):
                continue

            self.code_funcs[func._cg_construct] = func


    def emit(self, code):
        self.code += code + '\n'

    def generate_code(self, root=None):
        if not root:
            root = self.ast

        code_func = self.code_funcs[root.construct]

        code_func(root)

        return self.code


#--------------------------------------------------
# FUNCTIONS
#--------------------------------------------------

def code_emitter(construct):
    def decorator(func):
        func._cg_construct = construct
        return func

    return decorator
