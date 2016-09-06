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

        print 'declared variable:', name, 'type:', type_

        return var

    def get_variable(self, name):
        if name in self.variables:
            return self.variables[name]

        if self.parent_scope:
            return self.parent_scope.get_variable(name)

    def is_declared(self, name):
        return ((name in self.variables)
             or (self.parent_scope and self.parent_scope.is_declared(name)))
