#-------------------------------------------------
# IMPORTS
#-------------------------------------------------

from lexing.lexer    import Lexer
from lexing.source   import StringSource
from parsing.parser  import Parser
from parsing.syntax  import *
from semantics.scope import Scope

#-------------------------------------------------
# CONSTANTS
#-------------------------------------------------

# Maybe we don't even need multiple passes?  Well, might be useful someday.
PASS_1 = 1
PASS_2 = 2
PASS_3 = 3
PASS_4 = 4

#-------------------------------------------------
# DECORATORS
#-------------------------------------------------

def analyzes(c, p):
    def decorator(func):
        func._na_pass      = p
        func._na_construct = c

        return func

    return decorator

#-------------------------------------------------
# CLASSES
#-------------------------------------------------

class SemanticAnalyzer(object):
    def __init__(self):
        self.analyzer_funcs = {}

        for s in dir(self):
            func = getattr(self, s, None)
            if not hasattr(func, '_na_construct'):
                continue

            p = func._na_pass
            c = func._na_construct

            if p not in self.analyzer_funcs:
                self.analyzer_funcs[p] = {}

            self.analyzer_funcs[p][c] = func

        self.cur_pass = 0
        self.scope = Scope()

        # Built-ins
        self.scope.decl_var('console' , 'string')
        self.scope.decl_var('file'    , 'string')
        self.scope.decl_var('process' , 'string')
        self.scope.decl_var('raw'     , 'string')
        self.scope.decl_var('readline', 'string')

        # Prevent warnings for built-ins being unused
        for s in self.scope.variables:
            self.scope.var(s).reads  = 1000
            self.scope.var(s).writes = 999

    def raw(self, code, target):
        pass

    def include(self, file_name):
        # FIXME: This crap needs to be cleaned up and moved into some other
        # function in another file.
        with open(file_name, 'r') as f:
            source = StringSource(f.read())

        lexer  = Lexer(source)
        parser = Parser(lexer)

        #smaragd.trace('generating syntax tree...')
        tree = parser.generate_ast()

        self.verify_internal(tree)

    def verify_internal(self, node):
        cur_pass = self.cur_pass

        for p in range(1, 5):
            self.cur_pass = p
            self.verify_single(node)

        self.cur_pass = cur_pass

    def verify(self, ast):
        self.verify_internal(ast)
        self.verify_scope(self.scope)

    def verify_scope(self, scope):
        for s in scope.variables:
            var = scope.var(s)

            # One read means the variable is never used (only assigned once).
            if var.reads <= var.writes:
                if var.type_ == 'func':
                    if scope.name:
                        smaragd.warning('function not used in {}: {}'.format(scope.name, var.name))
                    else:
                        smaragd.warning('function not used: {}'.format(var.name))
                else:
                    if scope.name:
                        smaragd.warning('variable not used in {}: {}'.format(scope.name, var.name))
                    else:
                        smaragd.warning('variable not used: {}'.format(var.name))

        for nested in scope.nested_scopes:
            self.verify_scope(nested)

    def verify_children(self, node):
        if not node.children:
            return

        for child in node.children:
            self.verify_single(child)

    def verify_single(self, node):
        p = self.cur_pass

        r = False
        if p in self.analyzer_funcs:
            funcs = self.analyzer_funcs[p]
            if node.construct in funcs:
                funcs[node.construct](node)
                r = True

        if not r:
            self.verify_children(node)

        # Store scope for next pass.
        node.scope = self.scope

    def enter_scope(self, name):
        self.scope = self.scope.nested_scope()
        self.scope.name = name

    def leave_scope(self):
        self.scope = self.scope.parent_scope

    @analyzes(ADD, PASS_2)
    def __add(self, node):
        a = node.children[0]
        b = node.children[1]

        if (a.construct in (INTEGER, STRING)
        and b.construct in (INTEGER, STRING)
        and a.construct != b.construct):
            smaragd.warning('adding integer and string', node.token)

        self.verify_children(node)

    @analyzes(ASSIGN, PASS_1)
    def __assign(self, node):
        if node.children[0].construct == IDENTIFIER:
            var_name = node.children[0].data
            var = self.scope.var(var_name)
            if not var:
                # FIXME: Keep type data?
                self.scope.decl_var(var_name, 'string')
            var = self.scope.var(var_name)
            var.writes += 1

        self.verify_children(node)

    @analyzes(FUNC, PASS_1)
    def __func(self, node):
        scope_name = None

        if node.data:
            self.scope.decl_var(node.data, 'func')
            scope_name = 'function ' + node.data

        self.enter_scope(scope_name)

        decl = node.children[0]
        defi = node.children[1]

        if len(decl.children) > 9:
            # This is actually a limitation in Batch files, but since we want
            # portability we have to stick to the lowest common denominator.
            smaragd.error('functions cannot have more than 9 parameters')

        for child in decl.children:
            assert child.construct == IDENTIFIER
            # Start with 1 write since they are actually given values when
            # function is called.
            self.scope.decl_var(child.data, 'string').writes = 1

        self.verify_children(node)

        self.leave_scope()

    @analyzes(FUNC_CALL, PASS_2)
    def __func_call(self, node):
        # First child is the function identifier.
        func_name = node.children[0].data

        var = node.scope.var(func_name)
        if var:
            var.reads += 1

        if func_name == 'include':
            # Function name and a string is required.
            if len(node.children) != 2:
                smaragd.error('include() takes exactly one argument', node.token)
                return

            if node.children[1].construct != STRING:
                smaragd.error('included file name must be a compile-time constant', node.token)
                return

            file_name = node.children[1].data

            self.include(file_name)

            return
        elif func_name == 'raw':
            if len(node.children) < 2 or len(node.children) > 3:
                smaragd.error('raw() takes one or two arguments', node.token)
                return

            if node.children[1].construct != STRING:
                smaragd.error('raw command must be a compile-time constant', node.token)
                return

            target = None
            if len(node.children) > 2:
                if node.children[2].construct != STRING:
                    smaragd.error('target must be a compile-time constant', node.token)
                else:
                    target = node.children[2].data
            else:
                smaragd.warning('using raw() without specifying target is non-portable')

        if len(node.children) > 10:
            smaragd.error('functions cannot take more than 9 arguments', node.token)

        self.verify_children(node)

    @analyzes(IDENTIFIER, PASS_2)
    def __identifier(self, node):
        var = node.scope.var(node.data)
        if not var:
            smaragd.error('identifier not declared: {}'.format(node.data), node.token)
        else:
            var.reads += 1

    @analyzes(DIVIDE, PASS_1)
    def __divide(self, node):
        a = node.children[0]
        b = node.children[1]

        if a.construct == STRING or b.construct == STRING:
            smaragd.error('division only allowed with integers', node.token)

        elif a.construct == INTEGER and b.construct == INTEGER:
            if int(b.data) == 0:
                smaragd.warning('division by zero', node.token)
            elif int(a.data) > int(b.data):
                smaragd.warning('division will result in zero', node.token)

        self.verify_children(node)

    @analyzes(MULTIPLY, PASS_1)
    def __multiply(self, node):
        a = node.children[0]
        b = node.children[1]

        if a.construct == STRING or b.construct == STRING:
            smaragd.error('multiplication only allowed with integers', node.token)

        self.verify_children(node)

    @analyzes(SUBTRACT, PASS_1)
    def __subtract(self, node):
        a = node.children[0]
        b = node.children[1]

        if a.construct == STRING or b.construct == STRING:
            smaragd.error('subtraction only allowed with integers', node.token)

        self.verify_children(node)
