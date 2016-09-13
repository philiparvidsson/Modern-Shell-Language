#--------------------------------------------------
# IMPORTS
#--------------------------------------------------

import collections

import smaragd

from ..codegenerator import code_emitter, CodeGenerator

from parsing import syntax

from semantics.scope    import Scope
from semantics.variable import INT, STR, Variable

from lexing.lexer  import Lexer
from lexing.source import StringSource

from parsing.parser import Parser

#--------------------------------------------------
# CONSTANTS
#--------------------------------------------------

REF = 'reference'
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
        self.loop_labels = []

        self.segments = collections.OrderedDict((
            ('pre' , ''),
            ('init', ''),
            ('decl', ''),
            ('code', '')
        ))

    def raw(self, code, target):
        if target:
            print smaragd.conf.option('--target'), target
            if smaragd.conf.option('--target') != target:
                # Maybe validate target?
                return

        self.emit(code)

    def include(self, file_name):
        # TODO: Provide some general compilation function so we can reuse flags here
        f = open(file_name)
        s = f.read()
        f.close()

        p = Parser(Lexer(StringSource(s)))
        ast = p.generate_ast()
        b = Batch(ast)
        b.tempvar_counter = self.tempvar_counter
        b.label_counter = self.label_counter
        b.generate_code()
        self.tempvar_counter = b.tempvar_counter
        self.label_counter = b.label_counter

        #top_scope = self.scope
        #while top_scope.parent_scope:
        #    top_scope = top_scope.parent_scope

        for varname, var in b.scope.variables.iteritems():
            self.decl_var(varname, var.type_)

        self.emit(b.segments['init'], 'init')
        self.emit(b.segments['decl'], 'decl')
        self.emit(b.segments['code'], 'code')

        # Don't kill the stack.
        self.push('include', STR)

    def check_builtin(self, name):
        try:
            mod = __import__('codegen.batch.builtins.' + name, fromlist=['emit_code'])
        except ImportError:
            mod = None

        if mod:
            old_scope = self.scope
            top_scope = self.scope
            while top_scope.parent_scope:
                top_scope = top_scope.parent_scope

            self.scope = top_scope

            mod.emit_code(self)

            self.scope = old_scope


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
        return self.decl_var(name, type_)

    def enter_scope(self):
        self.scope = self.scope.nested_scope()

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
            self.emit('set "{}.{}={}"'.format(temp.name, index, self.pop().value))
            index += 1

        self.emit('set "{}.length={}"'.format(temp.name, index))

        self.push(temp, VAR)

    @code_emitter(syntax.ARRAY_IDX)
    def __array_idx(self, node):
        self._gen_code(node.children[0])
        self._gen_code(node.children[1])

        b = self.pop().value
        a = self.pop_deref().value

        self.push('{}.{}'.format(a, b), REF)

    @code_emitter(syntax.ASSIGN)
    def __assign(self, node):
        ident = node.children[0]
        expr = node.children[1]

        self._gen_code(expr)

        b = self.pop_deref()

        # TODO: Is this sane?
        if ident.construct == syntax.IDENTIFIER:
            a = ident.data
            if not self.scope.is_decl(a):
                type_ = b.type_
                if type_ == REF:
                    type_ = VAR
                a = self.decl_var(a, type_).name
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
        s = 'set /a "{}={}^^{}"'
        self.emit(s.format(temp.name, a.value, b.value))
        self.push(temp, VAR)

    @code_emitter(syntax.BREAK)
    def __break(self, node):
        self.emit('goto {}_'.format(self.loop_labels[-1]))

    @code_emitter(syntax.CONTINUE)
    def __continue(self, node):
        self.emit('goto {}_continue'.format(self.loop_labels[-1]))

    @code_emitter(syntax.DEC)
    def __dec(self, node):
        self._gen_code(node.children[0])

        a = self.pop()
        b = self.deref(a)

        # Maybe this is hacky? Well, it seems to work.
        s = a.value
        if hasattr(a, 'var'):
            s = a.var.name

        temp = self.tempvar(INT)
        self.emit('set /a "{}={}"'.format(temp.name, b.value))
        self.emit('set /a "{}={}-1"'.format(s, b.value))
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
        self._gen_code(node.children[0])
        self._gen_code(node.children[1])

        b = self.pop_deref().value
        a = self.pop_deref().value

        temp = self.tempvar(INT)
        s = 'if "{}" equ "{}" (set /a {}=1) else (set /a {}=0)'
        self.emit(s.format(a, b, temp.name, temp.name))
        self.push(temp, VAR)

    @code_emitter(syntax.FOR)
    def __for(self, node):
        label = self.label()
        self.loop_labels.append(label)

        init = node.children[0]
        cond = node.children[1]
        loop = node.children[2]

        if init.construct != syntax.NOOP:
            self._gen_code(init)

        self.emit(':{}'.format(label))

        if cond.construct != syntax.NOOP:
            self._gen_code(cond)
            self.emit('if {} equ 0 (goto :{}_)'.format(self.pop().value, label))

        for expr in node.children[3:]:
            self._gen_code(expr)


        self.emit(':{}_continue'.format(label))
        if loop.construct != syntax.NOOP:
            self._gen_code(loop)

        self.emit('goto :{}'.format(label))
        self.emit(')')
        self.emit(':{}_'.format(label))

        self.loop_labels.pop()

    def decl_var(self, name, type_):
        var = self.scope.decl_var(name, type_)

        if self.scope.nesting > 0:
            var.name = var.name + '_%~2'

        return var

    @code_emitter(syntax.FUNC)
    def __func(self, node):
        func_name = node.data
        if not func_name:
            func_name = self.tempvar().name

        self.decl_var(func_name, STR)
        self.enter_scope()
        self.decl_var('this', STR)
        self.emit('set {}={}'.format(func_name, func_name), 'decl')
        self.emit('goto {}_'.format(func_name)),
        self.emit(':{}'.format(func_name))
        #self.emit('setlocal')

        params = node.children[0]
        body = node.children[1]

        # Start from 3 since first 2 args are reserved for impl.
        param_counter = 3
        for param in params.children:
            # TODO: Don't assume str here. Be water, my friend!
            var = self.decl_var(param.data, STR)
            var.name = param_counter
            param_counter += 1

        for expr in body.children:
            self._gen_code(expr)

        if not body.children or not body.children[-1].construct == syntax.RETURN:
            self.emit('set %~1=0')
            self.emit('goto :eof')
        #    self.emit('endlocal & (set %1=0)')
        #    self.emit('exit /b')
        self.emit(':{}_'.format(func_name))

        self.leave_scope()
        self.push(func_name, STR)

    @code_emitter(syntax.FUNC_CALL)
    def __func_call(self, node):
        args = []

        # The include function needs special treatment!
        if node.children[0].construct == syntax.IDENTIFIER and node.children[0].data == 'include':
            self.include(node.children[1].data)
            return

        if node.children[0].construct == syntax.IDENTIFIER and node.children[0].data == 'raw':
            target = None
            if len(node.children) > 2:
                target = node.children[2].data

            self.raw(node.children[1].data, target)
            return

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
        var = self.scope.var(func_name)

        if self.scope.nesting == 0:
            nesting = '!__call__!'
            self.emit('set /a __call__+=1')
        else:
            t = self.tempvar(INT)
            self.emit('set /a "{}=(1 + %~2)"'.format(t.name))
            self.emit('set /a __call__={}'.format(t.name))
            nesting = '!{}!'.format(t.name)

        s = 'call :{} {} {} {}'
        self.emit(s.format(func_name, temp.name, nesting, ' '.join(args)))
        self.push(temp, VAR)

    @code_emitter(syntax.GREATER)
    def __greater(self, node):
        self._gen_code(node.children[0])
        self._gen_code(node.children[1])

        b = self.pop_deref().value
        a = self.pop_deref().value

        temp = self.tempvar(INT)
        s = 'if {} gtr {} (set /a {}=1) else (set /a {}=0)'
        self.emit(s.format(a, b, temp.name, temp.name))
        self.push(temp, VAR)

    @code_emitter(syntax.GREATER_EQ)
    def __greater_eq(self, node):
        self._gen_code(node.children[0])
        self._gen_code(node.children[1])

        b = self.pop_deref().value
        a = self.pop_deref().value

        temp = self.tempvar(INT)
        s = 'if {} geq {} (set /a {}=1) else (set /a {}=0)'
        self.emit(s.format(a, b, temp.name, temp.name))
        self.push(temp, VAR)

    @code_emitter(syntax.IDENTIFIER)
    def __identifier(self, node):
        ident = node.data
        var = self.scope.var(ident)
        if not var:
            #self.builtins.check(self, ident)
            self.check_builtin(ident)
            var = self.scope.var(ident)
        self.push(var, VAR)

    @code_emitter(syntax.INC)
    def __inc(self, node):
        self._gen_code(node.children[0])

        a = self.pop()
        b = self.deref(a)

        # Maybe this is hacky? Well, it seems to work.
        s = a.value
        if hasattr(a, 'var'):
            s = a.var.name

        temp = self.tempvar(INT)
        self.emit('set /a "{}={}"'.format(temp.name, b.value))
        self.emit('set /a "{}={}+1"'.format(s, b.value))
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
        self._gen_code(node.children[0])
        self._gen_code(node.children[1])

        b = self.pop_deref().value
        a = self.pop_deref().value

        temp = self.tempvar(INT)
        s = 'if {} lss {} (set /a {}=1) else (set /a {}=0)'
        self.emit(s.format(a, b, temp.name, temp.name))
        self.push(temp, VAR)

    @code_emitter(syntax.LESS_EQ)
    def __less_eq(self, node):
        self._gen_code(node.children[0])
        self._gen_code(node.children[1])

        b = self.pop_deref().value
        a = self.pop_deref().value

        temp = self.tempvar(INT)
        s = 'if {} leq {} (set /a {}=1) else (set /a {}=0)'
        self.emit(s.format(a, b, temp.name, temp.name))
        self.push(temp, VAR)

    @code_emitter(syntax.LOGIC_AND)
    def __logic_and(self, node):
        a = node.children[0]
        b = node.children[1]

        self._gen_code(a)
        self.emit('if {} neq 0 ('.format(self.pop().value))
        self._gen_code(b)
        self.emit(')')

    @code_emitter(syntax.LOGIC_OR)
    def __logic_or(self, node):
        a = node.children[0]
        b = node.children[1]

        temp = self.tempvar(INT)

        self._gen_code(a)
        self.emit('set /a {}=0'.format(temp.name))
        self.emit('if {} neq 0 ('.format(self.pop().value))
        self.emit('set /a {}=1'.format(temp.name))
        self.emit(') else (')
        self._gen_code(b)
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

        b = self.pop_deref().value
        a = self.pop_deref().value

        temp = self.tempvar(INT)
        s = 'if "{}" neq "{}" (set /a {}=1) else (set /a {}=0)'
        self.emit(s.format(a, b, temp.name, temp.name))
        self.push(temp, VAR)

    @code_emitter(syntax.PROGRAM)
    def __program(self, node):
        self.emit('@echo off', 'pre')
        self.emit('setlocal EnableDelayedExpansion', 'pre')

        self.emit('set __call__=0', 'pre')

        for child in node.children:
            self._gen_code(child)

    @code_emitter(syntax.RETURN)
    def __return(self, node):
        self._gen_code(node.children[0])

        a = self.pop_deref()

        #self.emit('endlocal & (')

        if hasattr(a, 'var'):
            a.value = '!{}!'.format(a.var.name)

        s = 'set /a %1={}' if a.type_ == INT else 'set %1={}'
        self.emit(s.format(a.value))

        #self.emit(')')
        #self.emit('exit /b')
        self.emit('goto :eof')

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
        # FIXME: Come up with something more clever here. This code below is ugly af.
#        allowed_chars = '\'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 '
#        s = ''

#        for c in node.data:
#            if c == '!':
#                # Exclamation mark requires double-escape.
#                # TODO: Or does it!?
#                c = '^^!'
#            elif c not in allowed_chars:
#                c = '^' + c
#            s += c

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
        self.loop_labels.append(label)

        self.emit(':{}'.format(label))
        self.emit(':{}_continue'.format(label))
        self._gen_code(node.children[0])
        self.emit('if {} neq 0 ('.format(self.pop().value))

        for expr in node.children[1:]:
            self._gen_code(expr)

        self.emit('goto :{}'.format(label))
        self.emit(')')
        self.emit(':{}_'.format(label))

        self.loop_labels.pop()
