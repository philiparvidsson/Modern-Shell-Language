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
        self.includes = []

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
        self.global_scope = Scope()
        self.scope = self.global_scope

        # Built-ins
        self.scope.decl_var('process' , 'string')
        self.scope.decl_var('raw'     , 'string')

        # Prevent warnings for built-ins being unused
        for s in self.scope.variables:
            self.scope.var(s).reads  = 1000
            self.scope.var(s).writes = 999

    def include(self, file_name):
        s = mshl.find_include_file(file_name)

        if not s:
            mshl.error('cannot include {}: no such file exists'.format(file_name))
            return

        if s in self.includes:
            return

        self.includes.append(s)

        # FIXME: This crap needs to be cleaned up and moved into some other
        # function in another file.
        with open(s, 'r') as f:
            source = StringSource(f.read())

        lexer  = Lexer(source)
        parser = Parser(lexer)

        #mshl.trace('generating syntax tree...')
        tree = parser.generate_ast()

        old_srcfile = mshl.srcfile
        mshl.srcfile = file_name
        self.verify_internal(tree)
        mshl.srcfile = old_srcfile

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
            # Also, no warnings for vars with leading underscores.  They're used
            # for raw code implementation.
            if not var.name.startswith('_') and var.reads <= var.writes:
                # FIXME: should probably use this for unnamed functions too
                if hasattr(var, 'node'):
                    var.node.is_unused = True
                if var.type_ == 'func':
                    if scope.name:
                        mshl.warning('function not used in {}: {}'.format(scope.name, var.name))
                    else:
                        mshl.warning('function not used: {}'.format(var.name))
                else:
                    if scope.name:
                        mshl.warning('variable not used in {}: {}'.format(scope.name, var.name))
                    else:
                        mshl.warning('variable not used: {}'.format(var.name))

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

    @analyzes(ADD, PASS_1)
    def __add(self, node):
        a = node.children[0]
        b = node.children[1]

        if (a.construct in (INTEGER, STRING)
        and b.construct in (INTEGER, STRING)
        and a.construct != b.construct):
            mshl.warning('adding integer and string', node.token)

        self.verify_children(node)

    @analyzes(ASSIGN, PASS_2)
    def __assign(self, node):
        if node.children[0].construct == IDENTIFIER:
            var_name = node.children[0].data
            var = self.scope.var(var_name)
            if not var:
                # FIXME: Keep type data?
                self.scope.decl_var(var_name, 'string')

            var = self.scope.var(var_name)
            var.writes += 1
            var.node = node

        self.verify_children(node)

    @analyzes(FUNC, PASS_1)
    def __func(self, node):
        scope_name = None

        func = None
        if node.data:
            if self.scope.nesting > 0:
                # FIXME: Maybe replace nested named functions with assignments
                # of anonymous functions in parser?
                mshl.error('nested functions must be anonymous', node.token)
            if self.scope.is_decl(node.data):
                mshl.error('duplicate function name: {}'.format(node.data), node.token)
            func = self.global_scope.decl_var(node.data, 'func')
            func.node = node
            scope_name = 'function ' + node.data

        self.enter_scope(scope_name)

        decl = node.children[0]
        defi = node.children[1]

        if len(decl.children) > 6:
            # This is actually a limitation in Batch files, but since we want
            # portability we have to stick to the lowest common denominator.
            # Also, Batch supports 9 parameters but 3 are reserved for impl.
            mshl.error('functions cannot have more than 6 parameters')

        if func:
            func.num_args = len(decl.children)

        arg_names = []
        for child in decl.children:
            assert child.construct == IDENTIFIER
            if child.data in arg_names:
                mshl.error('duplicate arg name: {}'.format(child.data), child.token)
            arg_names.append(child.data)

            # Start with 1 write since they are actually given values when
            # function is called.
            self.scope.decl_var(child.data, 'string').writes = 1

        self.verify_children(node)

        self.leave_scope()

    @analyzes(FUNC_CALL, PASS_2)
    def __func_call(self, node):
        # First child is the function identifier.
        func_name = node.children[0].data

        func = node.scope.var(func_name)
        if func:
            func.reads += 1

        if func_name == 'include':
            # Function name and a string is required.
            if len(node.children) != 2:
                mshl.error('include() takes exactly one argument', node.token)
                return

            if node.children[1].construct != STRING:
                mshl.error('included file name must be a compile-time constant', node.token)
                return

            file_name = node.children[1].data

            self.include(file_name)

            return
        elif func_name == 'raw':
            if len(node.children) < 2 or len(node.children) > 3:
                mshl.error('raw() takes one or two arguments', node.token)
                return

            if node.children[1].construct != STRING:
                mshl.error('raw command must be a compile-time constant', node.token)
                return

            target = None
            if len(node.children) > 2:
                if node.children[2].construct != STRING:
                    mshl.error('target must be a compile-time constant', node.token)
                else:
                    target = node.children[2].data
            else:
                mshl.warning('using raw() without specifying target is non-portable')

        if hasattr(func, 'num_args') and len(node.children) != func.num_args+1:
            mshl.warning('function {} takes {} arguments'.format(func_name, func.num_args), node.token)

        self.verify_children(node)

    @analyzes(IDENTIFIER, PASS_2)
    def __identifier(self, node):
        var = node.scope.var(node.data)
        if not var:
            mshl.error('identifier not declared: {}'.format(node.data), node.token)
        else:
            var.reads += 1

    @analyzes(DIVIDE, PASS_1)
    def __divide(self, node):
        a = node.children[0]
        b = node.children[1]

        if a.construct == STRING or b.construct == STRING:
            mshl.error('division only allowed with integers', node.token)

        elif a.construct == INTEGER and b.construct == INTEGER:
            if int(b.data) == 0:
                mshl.warning('division by zero', node.token)
            elif int(a.data) > int(b.data):
                mshl.warning('division will result in zero', node.token)

        self.verify_children(node)

    @analyzes(MULTIPLY, PASS_1)
    def __multiply(self, node):
        a = node.children[0]
        b = node.children[1]

        if a.construct == STRING or b.construct == STRING:
            mshl.error('multiplication only allowed with integers', node.token)

        self.verify_children(node)

    @analyzes(SUBTRACT, PASS_1)
    def __subtract(self, node):
        a = node.children[0]
        b = node.children[1]

        if a.construct == STRING or b.construct == STRING:
            mshl.error('subtraction only allowed with integers', node.token)

        self.verify_children(node)
