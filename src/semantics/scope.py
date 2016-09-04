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

        self.param_counter = 0
        self.variables = {}

    def declare_parameter(self, name, type_):
        self.param_counter += 1
        var = Variable('~{}'.format(self.param_counter), type_)

        print 'declared parameter {} of type {} (index={})'.format(name, type_, self.param_counter)

        self.variables[name] = var

        return var

    def declare_variable(self, name, type_):
        var = Variable(name, type_)

        print 'declared variable {} of type {}'.format(name, type_)

        self.variables[name] = var

        return var

    def get_variable(self, name):
        if name in self.variables:
            return self.variables[name]
