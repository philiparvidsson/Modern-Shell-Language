#--------------------------------------------------
# IMPORTS
#--------------------------------------------------

from .codegenerator import code_emitter, CodeGenerator

from parsing import syntax

#--------------------------------------------------
# CLASSES
#--------------------------------------------------

class Batch(CodeGenerator):
    def __init__(self, ast):
        super(Batch, self).__init__(ast)

        self.value_stack = []
        self.tempvar_counter = 0

    def tempvar_name(self):
        self.tempvar_counter += 1
        return '_{}'.format(self.tempvar_counter)

    @code_emitter(syntax.ADD)
    def __add(self, node):
        lhs = node.children[0]
        rhs = node.children[1]

        self.generate_code(lhs)
        self.generate_code(rhs)

        temp = self.tempvar_name()
        self.emit('set /a {}={}+{}'.format(temp, self.value_stack.pop(), self.value_stack.pop()))
        self.value_stack.append('!{}!'.format(temp))

    @code_emitter(syntax.ASSIGN)
    def __assign(self, node):
        switches = []

        ident = node.children[0]
        expr = node.children[1]

        self.generate_code(ident)
        self.generate_code(expr)

        if switches:
            self.emit('set {} {}={}'.format(' '.join(switches), identifier, 'loool'))
        else:
            self.emit('set {}={}'.format(ident.data, self.value_stack.pop()))

    @code_emitter(syntax.FUNC)
    def __func(self, node):
        self.emit(':{}'.format(node.data))

        self.emit('exit /b')

    @code_emitter(syntax.FUNC_CALL)
    def __func_call(self, node):
        self.emit('call :{} args'.format(node.data))

    @code_emitter(syntax.IDENTIFIER)
    def __identifier(self, node):
        self.value_stack.append('!{}!'.format(node.data))

    @code_emitter(syntax.INTEGER)
    def __integer(self, node):
        self.value_stack.append(node.data)

    @code_emitter(syntax.PROGRAM)
    def __program(self, node):
        self.emit('setlocal enabledelayedexpansion')

        for child in node.children:
            self.generate_code(child)
