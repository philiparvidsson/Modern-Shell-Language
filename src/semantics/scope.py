#--------------------------------------------------
# CLASSES
#--------------------------------------------------

class Scope(object):
    def __init__(self, parent_scope=None):
        self.parent_scope = parent_scope

        self.variables = []

    def declare_variable(name, type_):
        var = Variable(name, type_)

        self.variables.append(var)
