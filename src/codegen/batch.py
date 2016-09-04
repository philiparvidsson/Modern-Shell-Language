#--------------------------------------------------
# IMPORTS
#--------------------------------------------------

from .codegenerator import code_emitter, CodeGenerator

from parsing import syntax

from semantics.scope    import Scope
from semantics.variable import INT, STR, Variable

#--------------------------------------------------
# CONSTANTS
#--------------------------------------------------

VAR = 'variable'

#--------------------------------------------------
# CLASSES
#--------------------------------------------------

class Batch(CodeGenerator):
    def __init__(self, ast):
        super(Batch, self).__init__(ast)

        self.tempvar_counter = 0
        self.value_stack = []
        self.scope = Scope()

    def tempvar(self, *args):
        type_ = INT
        for a in args:
            if a == STR:
                type_ = STR
                break

        self.tempvar_counter += 1

        name =  '_{}'.format(self.tempvar_counter)
        return self.scope.declare_variable(name, type_)

    def var_type(name, type_=None):
        if not type_:
            return self.var_types[name]

        self.var_types[name] = type_

    def push(self, value, type_):
        self.value_stack.append((value, type_))

    def pop(self):
        # FIXME: Clean this crap up.
        x = self.value_stack.pop()
        y = lambda: None;

        y.value = x[0]
        y.type_ = x[1]

        if y.type_ == VAR:
            y.type_ = y.value.type_
            y.value = '!{}!'.format(y.value.name)

        return y

    @code_emitter(syntax.ADD)
    def __add(self, node):
        lhs = node.children[0]
        rhs = node.children[1]

        self.generate_code(rhs)
        self.generate_code(lhs)

        a = self.pop()
        b = self.pop()

        temp = self.tempvar(a.type_, b.type_)

        switches = []

        # If all involved vars are integers, we do an arithmetic operation.
        if a.type_ == INT and b.type_ == INT:
            switches.append('/a')

        switches = ' '.join(switches)
        s = 'set {} {}={}+{}'
        self.emit(s.format(switches, temp.name, a.value, b.value))
        self.push(temp, VAR)

    @code_emitter(syntax.ASSIGN)
    def __assign(self, node):
        ident = node.children[0]
        expr = node.children[1]

        self.generate_code(expr)

        a = self.pop()
        var = self.scope.declare_variable(ident.data, a.type_)

        self.generate_code(ident)
        switches = []

        if a.type_ == INT:
            switches.append('/a')

        self.emit('set {} {}={}'.format(' '.join(switches), ident.data, a.value))

    @code_emitter(syntax.DIVIDE)
    def __divide(self, node):
        lhs = node.children[0]
        rhs = node.children[1]

        self.generate_code(rhs)
        self.generate_code(lhs)

        a = self.pop()
        b = self.pop()

        temp = self.tempvar(INT)

        # All divisions are arithmetic.  We have to trust the semantic analyzer
        # to have solved this for us.
        self.emit('set /a {}={}/{}'.format(temp.name, a.value, b.value))
        self.push(temp, VAR)

    @code_emitter(syntax.FUNC)
    def __func(self, node):
        self.emit(':{}'.format(node.data))

        self.emit('exit /b')

    @code_emitter(syntax.FUNC_CALL)
    def __func_call(self, node):
        if node.data == 'print':
            self.__print(node)
        #self.emit('call :{} args'.format(node.data))

    @code_emitter(syntax.IDENTIFIER)
    def __identifier(self, node):
        self.push(self.scope.get_variable(node.data), VAR)

    @code_emitter(syntax.INTEGER)
    def __integer(self, node):
        self.push(node.data, INT)

    @code_emitter(syntax.MULTIPLY)
    def __multiply(self, node):
        lhs = node.children[0]
        rhs = node.children[1]

        self.generate_code(rhs)
        self.generate_code(lhs)

        a = self.pop()
        b = self.pop()

        temp = self.tempvar(INT)

        # All multiplications are arithmetic.  We have to trust the semantic
        # analyzer to have solved this for us.
        self.emit('set /a {}={}*{}'.format(temp.name, a.value, b.value))
        self.push(temp, VAR)

    @code_emitter(syntax.PROGRAM)
    def __program(self, node):
        self.emit('setlocal enabledelayedexpansion')

        for child in node.children:
            self.generate_code(child)

    @code_emitter(syntax.STRING)
    def __string(self, node):
        self.push(node.data, STR)

    @code_emitter(syntax.SUBTRACT)
    def __subtract(self, node):
        lhs = node.children[0]
        rhs = node.children[1]

        self.generate_code(rhs)
        self.generate_code(lhs)

        a = self.pop()
        b = self.pop()

        temp = self.tempvar(INT)

        # All subtractions are arithmetic.  We have to trust the semantic
        # analyzer to have solved this for us.
        self.emit('set /a {}={}-{}'.format(temp.name, a.value, b.value))
        self.push(temp, VAR)

    #@func('print')
    def __print(self, node):
        args = []

        if node.children:
            for arg in reversed(node.children):
                self.generate_code(arg)

            num_args = len(node.children)
            for i in range(num_args):
                args.append(self.pop().value)

        self.emit('echo.{}'.format(' '.join(args)))
