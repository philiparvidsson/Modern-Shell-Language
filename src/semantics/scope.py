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

        self.name = None
        self.nested_scopes = []
        self.variables = {}
        self.nesting = 0

    def decl_var(self, name, type_):
        var = Variable(name, type_, self)
        self.variables[name] = var

        return var

    def var(self, name):
        if name in self.variables:
            return self.variables[name]

        if self.parent_scope:
            return self.parent_scope.var(name)

    def is_decl(self, name):
        return ((name in self.variables)
             or (self.parent_scope and self.parent_scope.is_decl(name)))

    def nested_scope(self):
        scope = Scope(self)
        scope.nesting = self.nesting+1
        self.nested_scopes.append(scope)
        return scope
