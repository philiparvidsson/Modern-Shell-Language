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

class Scope(object):
    def __init__(self):
        self.arg_map = dict()

    def reg_arg(self, name, index):
        self.arg_map[name] = index

    def arg_index(self, name):
        if name in self.arg_map:
            return self.arg_map[name]

        return name

class Bat(object):
    def __init__(self):
        self.code = ""
        self.returned_value = ""
        self.temp_index = 0
        self.function_names = []

        self.emit_code("@echo off")
        self.emit_code("setlocal enabledelayedexpansion")

        self.scope = None

    def emit_code(self, code):
        self.code += code + "\n"

    def return_value(self, value):
        self.returned_value = value

    def get_temp_var(self):
        self.temp_index += 1
        return "temp" + str(self.temp_index)

    def finish(self):
        self.emit_code("exit /b")

    def enter_scope(self):
        self.scope = Scope()

    def leave_scope(self):
        self.scope = None

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
    bat.function_names.append(node.value)
    bat.emit_code(":{}".format(node.value))
    bat.emit_code("setlocal")
    bat.enter_scope()

    arg_index = 1
    for arg in node.children[0].children:
        bat.scope.reg_arg(arg.value, "~{}".format(arg_index))
        arg_index += 1

    for expr in node.children[1:]:
        if expr.kind == lexer.RETURN:
            if len(expr.children) == 0:
                # todo: warn if expr is not the last child (unreachable code)
                break
            generate_code_internal(bat, expr.children[0])
            bat.emit_code("endlocal")
            bat.emit_code("exit /b {}".format(bat.returned_value))
            bat.leave_scope()
            return

        generate_code_internal(bat, expr)

    bat.emit_code("endlocal")
    bat.emit_code("exit /b")
    bat.leave_scope()

@transpiles(lexer.CALL)
def transpile_call(bat, node):
    args = []

    for arg_node in node.children:
        generate_code_internal(bat, arg_node)
        args.append(bat.returned_value)

    #bat.emit_code("cscript //Nologo stdlib/{}.vbs {}".format(node.value, " ".join(args)))

    funcname = node.value
    import os.path
    if os.path.isfile("lib/" + funcname + ".bat"):
        if len(args) == 0:
            bat.emit_code("call lib/{}.bat".format(funcname))
        else:
            bat.emit_code("call lib/{}.bat {}".format(funcname, " ".join(args)))
    elif os.path.isfile("lib/" + funcname + ".vbs"):
        if len(args) == 0:
            bat.emit_code("cscript //Nologo lib/{}.vbs".format(funcname))
        else:
            bat.emit_code("cscript //Nologo lib/{}.vbs {}".format(funcname, " ".join(args)))
    else:
        if len(args) == 0:
            bat.emit_code("call :{}".format(funcname))
        else:
            bat.emit_code("call :{} {}".format(funcname, " ".join(args)))
    bat.return_value("!errorlevel!")

@transpiles(lexer.IDENTIFIER)
def transpile_identifier(bat, node):
    varname = node.value
    if bat.scope:
        varname = bat.scope.arg_index(varname)
    bat.return_value("!{}!".format(varname))

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

    generate_code_internal(bat, lhs)
    lhs_code = bat.returned_value

    generate_code_internal(bat, rhs)
    rhs_code = bat.returned_value

    varname = bat.get_temp_var()
    bat.emit_code("set /a {}={}+{}".format(varname, lhs_code, rhs_code))
    bat.return_value("!{}!".format(varname))

@transpiles(lexer.MULTIPLY)
def transpile_multiply(bat, node):
    lhs = node.children[0]
    rhs = node.children[1]

    generate_code_internal(bat, lhs)
    lhs_code = bat.returned_value

    generate_code_internal(bat, rhs)
    rhs_code = bat.returned_value

    varname = bat.get_temp_var()
    bat.emit_code("set /a {}={}*{}".format(varname, lhs_code, rhs_code))
    bat.return_value("!{}!".format(varname))

@transpiles(lexer.SUBTRACT)
def transpile_subtract(bat, node):
    lhs = node.children[0]
    rhs = node.children[1]

    generate_code_internal(bat, lhs)
    lhs_code = bat.returned_value

    generate_code_internal(bat, rhs)
    rhs_code = bat.returned_value

    varname = bat.get_temp_var()
    bat.emit_code("set /a {}={}-{}".format(varname, lhs_code, rhs_code))
    bat.return_value("!{}!".format(varname))

@transpiles(lexer.DIVIDE)
def transpile_divide(bat, node):
    lhs = node.children[0]
    rhs = node.children[1]

    generate_code_internal(bat, lhs)
    lhs_code = bat.returned_value

    generate_code_internal(bat, rhs)
    rhs_code = bat.returned_value

    varname = bat.get_temp_var()
    bat.emit_code("set /a {}={}/{}".format(varname, lhs_code, rhs_code))
    bat.return_value("!{}!".format(varname))

@transpiles(lexer.ASSIGNMENT)
def transpile_assignment(bat, node):
    identifier_node = node.children[0]
    expression_node = node.children[1]

    generate_code_internal(bat, expression_node)

    bat.emit_code("set {}={}".format(identifier_node.value, bat.returned_value))
    transpile_identifier(bat, identifier_node)

def generate_code_internal(bat, ast):
    transpile_fn = translators[ast.kind]
    transpile_fn(bat, ast)

def generate_code(bat, ast):
    generate_code_internal(bat, ast)
