#--------------------------------------------------
# CONSTANTS
#--------------------------------------------------

INT = 'integer'
STR = 'string'

#--------------------------------------------------
# CLASSES
#--------------------------------------------------

class Variable(object):
    def __init__(self, name, type_, scope):
        self.name = name
        self.type_ = type_
        self.scope = scope

        self.reads  = 0
        self.writes = 0
