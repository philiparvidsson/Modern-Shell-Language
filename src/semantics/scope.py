#--------------------------------------------------
# IMPORTS
#--------------------------------------------------

from .variable import Variable

#--------------------------------------------------
# CLASSES
#--------------------------------------------------

class Scope(object):
    def __init__(self, parent_scope=None):
        self.parent_scope = parent_scope

        self.variables = {}

    def declare_variable(self, name, type_):
        var = Variable(name, type_)
        self.variables[name] = var

        return var

    def get_variable(self, name):
        if name in self.variables:
            return self.variables[name]
