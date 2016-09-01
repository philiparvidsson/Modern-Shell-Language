#-------------------------------------------------
# IMPORTS
#-------------------------------------------------

from . import lexer

#-------------------------------------------------
# GLOBALS
#-------------------------------------------------

translators = {}

#-------------------------------------------------
# FUNCTIONS
#-------------------------------------------------


def transpiles(node_kind):
    def decorator(func):
        def deco(node):
            return func(node)

        global translators
        translators[node_kind] = func

        return deco

    return decorator


@transpiles(lexer.ASSIGNMENT)
def assignment(node):
    identifier_node = node.children[0]
    literal_node    = node.children[1]

    print "set %{}={}".format(identifier_node.value, literal_node.value)

def generate_code(ast):
    transpile_fn = translators[ast.kind]

    transpile_fn(ast)
