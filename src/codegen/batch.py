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

REF = 'reference'
VAR = 'variable'

#--------------------------------------------------
# CLASSES
#--------------------------------------------------

class Builtins(object):
    def __init__(self):
        pass

    def check(self, parser, name):
        if name == 'console':
            self.console(parser)
        elif name == 'process':
            self.process(parser)
        elif name == 'readline':
            self.readline(parser)

    def console(self, parser):
        if not hasattr(self, 'console_var_'):
            temp = parser.tempvar()
            parser.scope.declare_variable('console', VAR).name = temp.name
            self.console_var_ = temp

            parser.emit(
'''
set {0}={0}
set {0}[log]={0}[log]
goto __after_print
:{0}[log]
setlocal
set ret=%1
set str=
:__print_next
if "%~2" equ "" (goto :__print_done)
set "str=%str%%~2 "
shift
goto :__print_next
:__print_done
if "%str%" neq "" (echo %str%)
endlocal & (set %ret%=0)
exit /b
:__after_print
'''.format(self.console_var_.name), 'decl')

        parser.scope.declare_variable('console', VAR).name = self.console_var_.name


    def process(self, parser):
        if not hasattr(self, 'process_var_'):
            temp = parser.tempvar()
            parser.scope.declare_variable('process', VAR).name = temp.name
            self.process_var_ = temp

            parser.emit(
'''
set {0}={0}
set {0}[exit]={0}[exit]
goto __after_exit
:{0}[exit]
set "errorlevel=%~2"
goto :eof
:__after_exit
'''.format(self.process_var_.name), 'decl')

        parser.scope.declare_variable('process', VAR).name = self.process_var_.name


    def readline(self, parser):
        if not hasattr(self, 'is_readline_declared'):
            self.is_readline_declared = True
            parser.emit(
'''
set readline=readline
goto __after_readline
:readline
setlocal
set ret=%1
set str=
:__readline_next
if "%2" equ "" (goto :__readline_done)
set "str=%str%%2 "
shift
goto :__readline_next
:__readline_done
set /p tmp=%str%
endlocal & (set %ret%=%tmp%)
exit /b
:__after_readline
''', 'decl')

        parser.scope.declare_variable('readline', VAR)


class Batch(CodeGenerator):
    def __init__(self, ast):
        super(Batch, self).__init__(ast)

        self.builtins = Builtins()

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
            y.type_ = y.var.type_
            if isinstance(y.value.name, int):
                # Function parameters.
                y.value = '%~{}'.format(y.value.name)
            else:
                y.value = '!{}!'.format(y.value.name)

        y.value = str(y.value)
        return y

    def pop_deref(self):
        return self.deref(self.pop())

    def deref(self, a):
        if a.type_ == REF:
            temp = self.tempvar(STR)
            self.emit('call set "{}=%%{}%%"'.format(temp.name, a.value))

            y = lambda: None
            y.var = temp
            y.type_ = temp.type_
            y.value = '!{}!'.format(temp.name)

            y.value = str(y.value)

            return y

        return a

    @code_emitter(syntax.ADD)
    def __add(self, node):
        self._gen_code(node.children[0])
        self._gen_code(node.children[1])

        b = self.pop_deref()
        a = self.pop_deref()

        temp = self.tempvar(a.type_, b.type_)

        # If all involved vars are integers, we do an arithmetic operation.
        if a.type_ == INT and b.type_ == INT:
            s = 'set /a "{}={}+{}"'
        else:
            s = 'set "{}={}{}"'

        self.emit(s.format(temp.name, a.value, b.value))
        self.push(temp, VAR)


    @code_emitter(syntax.ARRAY)
    def __array(self, node):
        temp = self.tempvar(STR)
        self.emit('set "{}={}"'.format(temp.name, temp.name))

        index = 0
        for item in node.children:
            self._gen_code(item)
            self.emit('set "{}[{}]={}"'.format(temp.name, index, self.pop().value))
            index += 1

        self.emit('set "{}[__length__]={}"'.format(temp.name, index))

        self.push(temp, VAR)

    @code_emitter(syntax.ARRAY_IDX)
    def __array_idx(self, node):
        self._gen_code(node.children[0])
        self._gen_code(node.children[1])

        b = self.pop().value
        a = self.pop_deref().value

        # TODO: Do we have to default to str here?
        #temp = self.tempvar(STR)
        #self.emit('call set "{}=%%{}[{}]%%"'.format(temp.name, a, b))
        #self.push(temp, VAR)
        self.push('{}[{}]'.format(a, b), REF)

    @code_emitter(syntax.ASSIGN)
    def __assign(self, node):
        ident = node.children[0]
        expr = node.children[1]

        self._gen_code(expr)

        b = self.pop_deref()

        # TODO: Is this sane?
        if ident.construct == syntax.IDENTIFIER:
            a = ident.data
            if not self.scope.is_declared(ident.data):
                type_ = b.type_
                if type_ == REF:
                    type_ = VAR
                self.scope.declare_variable(ident.data, type_)
        else:
            self._gen_code(ident)
            a = self.pop().value

        self._gen_code(ident)
        switches = []

        if b.type_ == INT:
            switches.append('/a')

        self.emit('set {} "{}={}"'.format(' '.join(switches), a, b.value))
        #self.push(var, VAR)

    @code_emitter(syntax.BIN_AND)
    def __bin_and(self, node):
        self._gen_code(node.children[0])
        self._gen_code(node.children[1])

        b = self.pop_deref()
        a = self.pop_deref()

        temp = self.tempvar(INT)
        s = 'set /a "{}={}&{}"'
        self.emit(s.format(temp.name, a.value, b.value))
        self.push(temp, VAR)

    @code_emitter(syntax.BIN_OR)
    def __bin_or(self, node):
        self._gen_code(node.children[0])
        self._gen_code(node.children[1])

        b = self.pop_deref()
        a = self.pop_deref()

        temp = self.tempvar(INT)
        s = 'set /a "{}={}|{}"'
        self.emit(s.format(temp.name, a.value, b.value))
        self.push(temp, VAR)

    @code_emitter(syntax.BIN_XOR)
    def __bin_xor(self, node):
        self._gen_code(node.children[0])
        self._gen_code(node.children[1])

        b = self.pop_deref()
        a = self.pop_deref()

        temp = self.tempvar(INT)
        s = 'set /a "{}={}^{}"'
        self.emit(s.format(temp.name, a.value, b.value))
        self.push(temp, VAR)

    @code_emitter(syntax.DEC)
    def __dec(self, node):
        self._gen_code(node.children[0])

        a = self.pop()

        temp = self.tempvar(INT)
        self.emit('set /a "{}={}"'.format(temp.name, a.value))
        self.emit('set /a "{}={}-1"'.format(a.var.name, a.value))
        self.push(temp, VAR)

    @code_emitter(syntax.DIVIDE)
    def __divide(self, node):
        self._gen_code(node.children[0])
        self._gen_code(node.children[1])

        b = self.pop_deref()
        a = self.pop_deref()

        temp = self.tempvar(INT)
        s = 'set /a "{}={}/{}"'
        self.emit(s.format(temp.name, a.value, b.value))
        self.push(temp, VAR)

    @code_emitter(syntax.EQUAL)
    def __equal(self, node):
        lhs = node.children[0]
        rhs = node.children[1]

        self._gen_code(rhs)
        self._gen_code(lhs)

        temp = self.tempvar(INT)
        s = 'if {} equ {} (set /a {}=1) else (set /a {}=0)'
        self.emit(s.format(self.pop_deref().value, self.pop_deref().value, temp.name, temp.name))
        self.push(temp, VAR)

    @code_emitter(syntax.FUNC)
    def __func(self, node):
        func_name = node.data
        if not func_name:
            func_name = self.tempvar().name

        self.scope.declare_variable(func_name, STR)
        self.enter_scope()
        self.scope.declare_variable('this', STR)
        self.emit('set {}={}'.format(func_name, func_name), 'decl')
        self.emit('goto :__after_{}'.format(func_name)),
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
        self.emit(':__after_{}'.format(func_name))

    @code_emitter(syntax.FUNC_CALL)
    def __func_call(self, node):
        args = []

        self._gen_code(node.children[0])

        func_name = self.pop_deref().value
        #self.emit('set this={}'.format(func_name))

        for arg in node.children[1:]:
            self._gen_code(arg)

        num_args = len(node.children)
        for i in range(1, num_args):
            a = self.pop_deref()
            if a.type_ == STR:
                args.append('"{}"'.format(a.value))
            else:
                args.append(a.value)

        args.reverse()

        temp = self.tempvar(STR) # FIXME: Don't assume str!
        var = self.scope.get_variable(func_name)

        s = 'call :{} {} {}'
        self.emit(s.format(func_name, temp.name, ' '.join(args)))
        self.push(temp, VAR)

    @code_emitter(syntax.GREATER)
    def __greater(self, node):
        self._gen_code(node.children[0])
        self._gen_code(node.children[1])

        temp = self.tempvar(INT)
        s = 'if {} gtr {} (set /a {}=1) else (set /a {}=0)'
        self.emit(s.format(self.pop_deref().value, self.pop_deref().value, temp.name, temp.name))
        self.push(temp, VAR)

    @code_emitter(syntax.GREATER_EQ)
    def __greater_eq(self, node):
        self._gen_code(node.children[0])
        self._gen_code(node.children[1])

        temp = self.tempvar(INT)
        s = 'if {} geq {} (set /a {}=1) else (set /a {}=0)'
        self.emit(s.format(self.pop_deref().value, self.pop_deref().value, temp.name, temp.name))
        self.push(temp, VAR)

    @code_emitter(syntax.IDENTIFIER)
    def __identifier(self, node):
        ident = node.data
        var = self.scope.get_variable(ident)
        if not var:
            self.builtins.check(self, ident)
            var = self.scope.get_variable(ident)
        self.push(var, VAR)

    @code_emitter(syntax.INC)
    def __inc(self, node):
        self._gen_code(node.children[0])

        a = self.pop()
        b = self.deref(a)

        temp = self.tempvar(INT)
        self.emit('set /a "{}={}"'.format(temp.name, b.value))
        self.emit('set /a "{}={}+1"'.format(a.var.name, b.value))
        self.push(temp, VAR)

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

    @code_emitter(syntax.IF_TERNARY)
    def __if_ternary(self, node):
        cond = node.children[0]
        then_expr = node.children[1]
        else_expr = node.children[2]

        self._gen_code(cond)

        temp = self.tempvar(STR)
        both_int = False

        self.emit('if {} neq 0 ('.format(self.pop().value))
        self._gen_code(then_expr)
        a = self.pop()
        self.emit('set "{}={}"'.format(temp.name, a.value))
        self.emit(') else (')
        self._gen_code(else_expr)
        b = self.pop()
        self.emit('set "{}={}"'.format(temp.name, b.value))
        self.emit(')')

        if a.type_ == INT and b.type_ == INT:
            temp.type_ = INT

        self.push(temp, VAR)

    @code_emitter(syntax.INTEGER)
    def __integer(self, node):
        self.push(node.data, INT)

    @code_emitter(syntax.LESS)
    def __less(self, node):
        self._gen_code(node.children[1])
        self._gen_code(node.children[0])

        temp = self.tempvar(INT)
        s = 'if {} lss {} (set /a {}=1) else (set /a {}=0)'
        self.emit(s.format(self.pop_deref().value, self.pop_deref().value, temp.name, temp.name))
        self.push(temp, VAR)

    @code_emitter(syntax.LESS_EQ)
    def __less_eq(self, node):
        self._gen_code(node.children[0])
        self._gen_code(node.children[1])

        temp = self.tempvar(INT)
        s = 'if {} leq {} (set /a {}=1) else (set /a {}=0)'
        self.emit(s.format(self.pop_deref().value, self.pop_deref().value, temp.name, temp.name))
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

        b = self.pop_deref()
        a = self.pop_deref()

        temp = self.tempvar(INT)
        s = 'set /a "{}={}%%{}"'
        self.emit(s.format(temp.name, a.value, b.value))
        self.push(temp, VAR)

    @code_emitter(syntax.MULTIPLY)
    def __multiply(self, node):
        self._gen_code(node.children[0])
        self._gen_code(node.children[1])

        b = self.pop_deref()
        a = self.pop_deref()

        temp = self.tempvar(INT)
        s = 'set /a "{}={}*{}"'
        self.emit(s.format(temp.name, a.value, b.value))
        self.push(temp, VAR)

    @code_emitter(syntax.NOT_EQ)
    def __not_eq(self, node):
        self._gen_code(node.children[0])
        self._gen_code(node.children[1])

        temp = self.tempvar(INT)
        s = 'if {} neq {} (set /a {}=1) else (set /a {}=0)'
        self.emit(s.format(self.pop_deref().value, self.pop_deref().value, temp.name, temp.name))
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

        a = self.pop_deref()

        self.emit('endlocal & (')
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

        b = self.pop_deref()
        a = self.pop_deref()

        temp = self.tempvar(INT)
        s = 'set /a "{}={}<<{}"'
        self.emit(s.format(temp.name, a.value, b.value))
        self.push(temp, VAR)

    @code_emitter(syntax.SHIFT_R)
    def __shift_r(self, node):
        self._gen_code(node.children[0])
        self._gen_code(node.children[1])

        b = self.pop_deref()
        a = self.pop_deref()

        temp = self.tempvar(INT)
        s = 'set /a "{}={}>>{}"'
        self.emit(s.format(temp.name, a.value, b.value))
        self.push(temp, VAR)

    @code_emitter(syntax.STRING)
    def __string(self, node):
        self.push('{}'.format(node.data), STR)

    @code_emitter(syntax.SUBTRACT)
    def __subtract(self, node):
        self._gen_code(node.children[0])
        self._gen_code(node.children[1])

        b = self.pop_deref()
        a = self.pop_deref()

        temp = self.tempvar(INT)
        s = 'set /a "{}={}-{}"'
        self.emit(s.format(temp.name, a.value, b.value))
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

#--------------------------------------------------
# FUNCTIONS
#--------------------------------------------------
