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
        self.temp_index = 0

        self.emit_code("setlocal")

    def emit_code(self, code):
        self.code += code + "\n"

    def return_value(self, value):
        self.returned_value = value

    def get_temp_var(self):
        self.temp_index += 1
        return "temp" + str(self.temp_index)

#-------------------------------------------------
# FUNCTIONS
#-------------------------------------------------

def transpiles(node_kind):
    def decorator(func):
        global translators
        translators[node_kind] = func

        return func

    return decorator

@transpiles(lexer.FUNC)
def transpile_func(bat, node):
    bat.emit_code(":{}".format(node.value))
    bat.emit_code("setlocal")
    for expr in node.children:
        if expr.kind == lexer.RETURN:
            if len(expr.children) == 0:
                # todo: warn if expr is not the last child (unreachable code)
                break
            generate_code(bat, expr.children[0])
            bat.emit_code("endlocal")
            bat.emit_code("exit /b {}".format(bat.returned_value))
            return

        generate_code(bat, expr)

    bat.emit_code("endlocal")
    bat.emit_code("exit /b")

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
def transpile_add(bat, node):
    lhs = node.children[0]
    rhs = node.children[1]

    generate_code(bat, lhs)
    lhs_code = bat.returned_value

    generate_code(bat, rhs)
    rhs_code = bat.returned_value

    varname = bat.get_temp_var()
    bat.emit_code("set /a {}={}+{}".format(varname, lhs_code, rhs_code))
    bat.return_value("!{}!".format(varname))

@transpiles(lexer.MULTIPLY)
def transpile_multiply(bat, node):
    lhs = node.children[0]
    rhs = node.children[1]

    generate_code(bat, lhs)
    lhs_code = bat.returned_value

    generate_code(bat, rhs)
    rhs_code = bat.returned_value

    varname = bat.get_temp_var()
    bat.emit_code("set /a {}={}*{}".format(varname, lhs_code, rhs_code))
    bat.return_value("!{}!".format(varname))

@transpiles(lexer.SUBTRACT)
def transpile_subtract(bat, node):
    lhs = node.children[0]
    rhs = node.children[1]

    generate_code(bat, lhs)
    lhs_code = bat.returned_value

    generate_code(bat, rhs)
    rhs_code = bat.returned_value

    varname = bat.get_temp_var()
    bat.emit_code("set /a {}={}-{}".format(varname, lhs_code, rhs_code))
    bat.return_value("!{}!".format(varname))

@transpiles(lexer.DIVIDE)
def transpile_divide(bat, node):
    lhs = node.children[0]
    rhs = node.children[1]

    generate_code(bat, lhs)
    lhs_code = bat.returned_value

    generate_code(bat, rhs)
    rhs_code = bat.returned_value

    varname = bat.get_temp_var()
    bat.emit_code("set /a {}={}/{}".format(varname, lhs_code, rhs_code))
    bat.return_value("!{}!".format(varname))

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
