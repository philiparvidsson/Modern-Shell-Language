#--------------------------------------------------
# IMPORTS
#--------------------------------------------------

from parsing.syntax import NOOP

#--------------------------------------------------
# CLASSES
#--------------------------------------------------

class CodeGenerator(object):
    def __init__(self, ast):
        self.ast = ast
        self.code_funcs = dict()

        for s in dir(self):
            func = getattr(self, s, None)
            if not hasattr(func, '_cg_construct'):
                continue

            self.code_funcs[func._cg_construct] = func

    def code(self):
        assert False, "Not implemented"

    def _gen_code(self, root):
        if root.construct == NOOP:
            return

        code_func = self.code_funcs[root.construct]
        code_func(root)

    def generate_code(self):
        self._gen_code(self.ast)

        return self.code()

#--------------------------------------------------
# FUNCTIONS
#--------------------------------------------------

def code_emitter(construct):
    def decorator(func):
        func._cg_construct = construct
        return func

    return decorator
