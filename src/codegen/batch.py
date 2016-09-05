#--------------------------------------------------
# IMPORTS
#--------------------------------------------------

import collections

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

        self.label_counter = 0
        self.tempvar_counter = 0
        self.value_stack = []
        self.scope = Scope()

        self.segments = collections.OrderedDict((
            ('init', ''),
            ('decl', ''),
            ('code', '')

        ))

    def code(self):
        code = ''

        for s in self.segments:
            code += self.segments[s] + '\n'

        return code

    def emit(self, code, segment='code'):
        if segment not in self.segments:
            self.segments[segment] = ''

        self.segments[segment] += code + '\n'

    def label(self):
        self.label_counter += 1

        return 'lbl{}'.format(self.label_counter)

    def tempvar(self, *args):
        type_ = INT
        for a in args:
            if a == STR:
                type_ = STR
                break

        self.tempvar_counter += 1

        name =  '__{}'.format(self.tempvar_counter)
        return self.scope.declare_variable(name, type_)

    def enter_scope(self):
        self.scope = Scope(self.scope)

    def leave_scope(self):
        self.scope = self.scope.parent_scope

    def push(self, value, type_):
        self.value_stack.append((value, type_))

    def pop(self):
        # FIXME: Clean this crap up.
        x = self.value_stack.pop()
        y = lambda: None;

        y.value = x[0]
        y.type_ = x[1]

        if y.type_ == VAR:
            y.var = y.value
            y.type_ = y.value.type_
            if isinstance(y.value.name, int):
                # Function parameters.
                y.value = '%{}'.format(y.value.name)
            else:
                y.value = '!{}!'.format(y.value.name)

        y.value = str(y.value)
        return y

    @code_emitter(syntax.ADD)
    def __add(self, node):
        lhs = node.children[0]
        rhs = node.children[1]

        self._gen_code(rhs)
        self._gen_code(lhs)

        a = self.pop()
        b = self.pop()

        temp = self.tempvar(a.type_, b.type_)

        # If all involved vars are integers, we do an arithmetic operation.
        if a.type_ == INT and b.type_ == INT:
            s = 'set /a "{}={}+{}"'
        else:
            s = 'set "{}={}{}"'

        self.emit(s.format(temp.name, a.value, b.value))
        self.push(temp, VAR)

    @code_emitter(syntax.ASSIGN)
    def __assign(self, node):
        ident = node.children[0]
        expr = node.children[1]

        self._gen_code(expr)

        a = self.pop()
        var = self.scope.declare_variable(ident.data, a.type_)

        self._gen_code(ident)
        switches = []

        if a.type_ == INT:
            switches.append('/a')

        self.emit('set {} {}={}'.format(' '.join(switches), ident.data, a.value))
        #self.push(var, VAR)

    @code_emitter(syntax.BIN_AND)
    def __bin_and(self, node):
        self._gen_code(node.children[0])
        self._gen_code(node.children[1])

        temp = self.tempvar(INT)
        s = 'set /a "{}={}&{}"'
        self.emit(s.format(temp.name, self.pop().value, self.pop().value))
        self.push(temp, VAR)

    @code_emitter(syntax.BIN_OR)
    def __bin_or(self, node):
        self._gen_code(node.children[0])
        self._gen_code(node.children[1])

        temp = self.tempvar(INT)
        s = 'set /a "{}={}|{}"'
        self.emit(s.format(temp.name, self.pop().value, self.pop().value))
        self.push(temp, VAR)

    @code_emitter(syntax.BIN_XOR)
    def __bin_xor(self, node):
        self._gen_code(node.children[0])
        self._gen_code(node.children[1])

        temp = self.tempvar(INT)
        s = 'set /a "{}={}^{}"'
        self.emit(s.format(temp.name, self.pop().value, self.pop().value))
        self.push(temp, VAR)

    @code_emitter(syntax.DIVIDE)
    def __divide(self, node):
        self._gen_code(node.children[0])
        self._gen_code(node.children[1])

        temp = self.tempvar(INT)
        s = 'set /a "{}={}/{}"'
        self.emit(s.format(temp.name, self.pop().value, self.pop().value))
        self.push(temp, VAR)

    @code_emitter(syntax.EQUAL)
    def __equal(self, node):
        lhs = node.children[0]
        rhs = node.children[1]

        self._gen_code(rhs)
        self._gen_code(lhs)

        temp = self.tempvar(INT)
        s = 'if {} equ {} (set /a {}=1) else (set /a {}=0)'
        self.emit(s.format(self.pop().value, self.pop().value, temp.name, temp.name))
        self.push(temp, VAR)

    @code_emitter(syntax.FUNC)
    def __func(self, node):
        func_name = node.data
        if not func_name:
            func_name = self.tempvar().name

        self.scope.declare_variable(func_name, STR)
        self.enter_scope()
        self.emit('set {}={}'.format(func_name, func_name), 'decl')
        self.emit('goto :{}_skip'.format(func_name)),
        self.emit(':{}'.format(func_name))
        self.emit('setlocal')

        params = node.children[0]
        body = node.children[1]

        param_counter = 2
        for param in params.children:
            # TODO: Don't assume str here. Be water, my friend!
            var = self.scope.declare_variable(param.data, STR)
            var.name = param_counter
            param_counter += 1

        for expr in body.children:
            self._gen_code(expr)

        if not body.children or not body.children[-1].construct == syntax.RETURN:
            self.emit('endlocal & (set %1=0)')
            self.emit('exit /b')
        self.leave_scope()
        self.push(func_name, STR)
        self.emit(':{}_skip'.format(func_name))

    @code_emitter(syntax.FUNC_CALL)
    def __func_call(self, node):
        args = []

        for arg in reversed(node.children):
            self._gen_code(arg)

        num_args = len(node.children)
        for i in range(num_args):
            args.append(self.pop().value)

        temp = self.tempvar(STR) # FIXME: Don't assume str!
        var = self.scope.get_variable(args[0])
        self.emit('call :{} {} {}'.format(args[0], temp.name, ' '.join(args[1:])))
        self.push(temp, VAR)

    @code_emitter(syntax.GREATER)
    def __greater(self, node):
        lhs = node.children[0]
        rhs = node.children[1]

        self._gen_code(rhs)
        self._gen_code(lhs)

        temp = self.tempvar(INT)
        s = 'if {} gtr {} (set /a {}=1) else (set /a {}=0)'
        self.emit(s.format(self.pop().value, self.pop().value, temp.name, temp.name))
        self.push(temp, VAR)

    @code_emitter(syntax.GREATER_EQ)
    def __greater_eq(self, node):
        lhs = node.children[0]
        rhs = node.children[1]

        self._gen_code(rhs)
        self._gen_code(lhs)

        temp = self.tempvar(INT)
        s = 'if {} geq {} (set /a {}=1) else (set /a {}=0)'
        self.emit(s.format(self.pop().value, self.pop().value, temp.name, temp.name))
        self.push(temp, VAR)

    @code_emitter(syntax.IDENTIFIER)
    def __identifier(self, node):
        ident = node.data
        self.push(self.scope.get_variable(node.data), VAR)

    @code_emitter(syntax.IF)
    def __if(self, node):
        cond = node.children[0]
        then_expr = node.children[1]
        else_expr = node.children[2]

        self._gen_code(cond)

        self.emit('if {} neq 0 ('.format(self.pop().value))

        for expr in then_expr.children:
            self._gen_code(expr)

        if len(else_expr.children) > 0:
            self.emit(') else (')

            for expr in else_expr.children:
                self._gen_code(expr)

        self.emit(')')

    @code_emitter(syntax.INTEGER)
    def __integer(self, node):
        self.push(node.data, INT)

    @code_emitter(syntax.LESS)
    def __less(self, node):
        lhs = node.children[0]
        rhs = node.children[1]

        self._gen_code(rhs)
        self._gen_code(lhs)

        temp = self.tempvar(INT)
        s = 'if {} lss {} (set /a {}=1) else (set /a {}=0)'
        self.emit(s.format(self.pop().value, self.pop().value, temp.name, temp.name))
        self.push(temp, VAR)

    @code_emitter(syntax.LESS_EQ)
    def __less_eq(self, node):
        lhs = node.children[0]
        rhs = node.children[1]

        self._gen_code(rhs)
        self._gen_code(lhs)

        temp = self.tempvar(INT)
        s = 'if {} leq {} (set /a {}=1) else (set /a {}=0)'
        self.emit(s.format(self.pop().value, self.pop().value, temp.name, temp.name))
        self.push(temp, VAR)

    @code_emitter(syntax.LOGIC_AND)
    def __logic_and(self, node):
        cond = node.children[0]
        then_expr = node.children[1]

        self._gen_code(cond)
        self.emit('if {} neq 0 ('.format(self.pop().value))
        self._gen_code(then_expr)
        self.emit(')')

    @code_emitter(syntax.LOGIC_OR)
    def __logic_or(self, node):
        cond = node.children[0]
        then_expr = node.children[1]

        temp = self.tempvar(INT)

        self._gen_code(cond)
        self.emit('set /a {}=0'.format(temp.name))
        self.emit('if {} neq 0 ('.format(self.pop().value))
        self.emit('set /a {}=1'.format(temp.name))
        self.emit(') else (')
        self._gen_code(then_expr)
        self.emit('if {} neq 0 ('.format(self.pop().value))
        self.emit('set /a {}=1'.format(temp.name))
        self.emit(')')
        self.emit(')')
        self.push(temp, VAR)

    @code_emitter(syntax.MODULO)
    def __modulo(self, node):
        self._gen_code(node.children[0])
        self._gen_code(node.children[1])

        temp = self.tempvar(INT)
        s = 'set /a "{}={}%{}"'
        self.emit(s.format(temp.name, self.pop().value, self.pop().value))
        self.push(temp, VAR)

    @code_emitter(syntax.MULTIPLY)
    def __multiply(self, node):
        self._gen_code(node.children[0])
        self._gen_code(node.children[1])

        temp = self.tempvar(INT)
        s = 'set /a "{}={}*{}"'
        self.emit(s.format(temp.name, self.pop().value, self.pop().value))
        self.push(temp, VAR)

    @code_emitter(syntax.NOT_EQ)
    def __not_eq(self, node):
        lhs = node.children[0]
        rhs = node.children[1]

        self._gen_code(rhs)
        self._gen_code(lhs)

        temp = self.tempvar(INT)
        s = 'if {} neq {} (set /a {}=1) else (set /a {}=0)'
        self.emit(s.format(self.pop().value, self.pop().value, temp.name, temp.name))
        self.push(temp, VAR)

    @code_emitter(syntax.PROGRAM)
    def __program(self, node):
        self.emit('@echo off', 'init')
        self.emit('setlocal enabledelayedexpansion', 'init')

        for child in node.children:
            self._gen_code(child)

    @code_emitter(syntax.RETURN)
    def __return(self, node):
        expr = node.children[0]
        self._gen_code(expr)
        self.emit('endlocal & (')

        a = self.pop()
        if a.type_ == INT:
            s = 'set /a %1={}'
        else:
            s = 'set %1={}'

        # FIXME: Clean this function up.

        if hasattr(a, 'var'):
            self.emit(s.format('%{}%'.format(a.var.name)))
        else:
            self.emit(s.format(a.value))

        self.emit(')')
        self.emit('exit /b')

    @code_emitter(syntax.SHIFT_L)
    def __shift_l(self, node):
        self._gen_code(node.children[0])
        self._gen_code(node.children[1])

        temp = self.tempvar(INT)
        s = 'set /a "{}={}<<{}"'
        self.emit(s.format(temp.name, self.pop().value, self.pop().value))
        self.push(temp, VAR)

    @code_emitter(syntax.SHIFT_R)
    def __shift_r(self, node):
        self._gen_code(node.children[0])
        self._gen_code(node.children[1])

        temp = self.tempvar(INT)
        s = 'set /a "{}={}>>{}"'
        self.emit(s.format(temp.name, self.pop().value, self.pop().value))
        self.push(temp, VAR)

    @code_emitter(syntax.STRING)
    def __string(self, node):
        self.push('{}'.format(node.data), STR)

    @code_emitter(syntax.SUBTRACT)
    def __subtract(self, node):
        self._gen_code(node.children[0])
        self._gen_code(node.children[1])

        temp = self.tempvar(INT)
        s = 'set /a "{}={}-{}"'
        self.emit(s.format(temp.name, self.pop().value, self.pop().value))
        self.push(temp, VAR)

    @code_emitter(syntax.WHILE)
    def __while(self, node):
        label = self.label()
        self.emit(':{}'.format(label))
        self._gen_code(node.children[0])
        self.emit('if {} neq 0 ('.format(self.pop().value))

        for expr in node.children[1:]:
            self._gen_code(expr)

        self.emit('goto :{}'.format(label))
        self.emit(')')
