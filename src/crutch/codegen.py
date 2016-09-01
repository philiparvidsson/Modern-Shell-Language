#-------------------------------------------------
# IMPORTS
#-------------------------------------------------

from . import lexer

#-------------------------------------------------
# GLOBALS
#-------------------------------------------------

translators = {}

#-------------------------------------------------
# CLASSES
#-------------------------------------------------

class Bat(object):
    def __init__(self):
        self.code = ""
        self.returned_code = ""

    def emit_code(self, code):
        self.code += code + "\n"

    def return_code(self, code):
        self.returned_code = code

#-------------------------------------------------
# FUNCTIONS
#-------------------------------------------------

def transpiles(node_kind):
    def decorator(func):
        def deco(bat, node):
            return func(bat, node)

        global translators
        translators[node_kind] = func

        return deco

    return decorator

@transpiles(lexer.IDENTIFIER)
def transpile_identifier(bat, node):
    bat.return_code("%{}%".format(node.value))

@transpiles(lexer.NUMERAL)
def transpile_numeral(bat, node):
    bat.return_code("{}".format(node.value))

@transpiles(lexer.STRING)
def transpile_string(bat, node):
    bat.return_code("\"{}\"".format(node.value))

@transpiles(lexer.ASSIGNMENT)
def transpile_assignment(bat, node):
    identifier_node = node.children[0]
    expression_node = node.children[1]

    generate_code(bat, expression_node)

    bat.emit_code("set /a {}={}".format(identifier_node.value, bat.returned_code))
    transpile_identifier(bat, identifier_node)

def generate_code(bat, ast):
    transpile_fn = translators[ast.kind]
    transpile_fn(bat, ast)
