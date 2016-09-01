#-------------------------------------------------
# IMPORTS
#-------------------------------------------------

from . import lexer

#-------------------------------------------------
# CONSTANTS
#-------------------------------------------------

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
        self.returned_value = ""

    def emit_code(self, code):
        self.code += code + "\n"

    def return_value(self, value):
        self.returned_value = value

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

@transpiles(lexer.CALL)
def transpile_call(bat, node):
    args = []

    for arg_node in node.children:
        generate_code(bat, arg_node)
        args.append(bat.returned_value)

    bat.emit_code("cscript //Nologo stdlib/{}.vbs {}".format(node.value, " ".join(args)))

@transpiles(lexer.IDENTIFIER)
def transpile_identifier(bat, node):
    bat.return_value("!{}!".format(node.value))

@transpiles(lexer.NUMERAL)
def transpile_numeral(bat, node):
    bat.return_value("{}".format(node.value))

@transpiles(lexer.STRING)
def transpile_string(bat, node):
    bat.return_value("{}".format(node.value))

@transpiles(lexer.ADD)
def transpile_assignment(bat, node):
    lhs = node.children[0]
    rhs = node.children[1]

    generate_code(bat, lhs)
    lhs_code = bat.returned_value

    generate_code(bat, rhs)
    rhs_code = bat.returned_value

    bat.return_value("{}+{}".format(lhs_code, rhs_code))

@transpiles(lexer.MULTIPLY)
def transpile_assignment(bat, node):
    lhs = node.children[0]
    rhs = node.children[1]

    generate_code(bat, lhs)
    lhs_code = bat.returned_value

    generate_code(bat, rhs)
    rhs_code = bat.returned_value

    bat.return_value("{}*{}".format(lhs_code, rhs_code))

@transpiles(lexer.SUBTRACT)
def transpile_assignment(bat, node):
    lhs = node.children[0]
    rhs = node.children[1]

    generate_code(bat, lhs)
    lhs_code = bat.returned_value

    generate_code(bat, rhs)
    rhs_code = bat.returned_value

    bat.return_value("{}-{}".format(lhs_code, rhs_code))

@transpiles(lexer.DIVIDE)
def transpile_assignment(bat, node):
    lhs = node.children[0]
    rhs = node.children[1]

    generate_code(bat, lhs)
    lhs_code = bat.returned_value

    generate_code(bat, rhs)
    rhs_code = bat.returned_value

    bat.return_value("{}/{}".format(lhs_code, rhs_code))

@transpiles(lexer.ASSIGNMENT)
def transpile_assignment(bat, node):
    identifier_node = node.children[0]
    expression_node = node.children[1]

    generate_code(bat, expression_node)

    bat.emit_code("set {}={}".format(identifier_node.value, bat.returned_value))
    transpile_identifier(bat, identifier_node)

def generate_code(bat, ast):
    transpile_fn = translators[ast.kind]
    transpile_fn(bat, ast)
