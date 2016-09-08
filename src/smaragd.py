#-------------------------------------------------
# IMPORTS
#-------------------------------------------------

import sys

from codegen.batch.batchgen import Batch
from debug.ast              import visualize_ast
from lexing.lexer           import Lexer
from lexing.source          import StringSource
from optim.astoptim         import ASTOptimizer
from parsing.parser         import Parser

#-------------------------------------------------
# GLOBALS
#-------------------------------------------------

config = None

#-------------------------------------------------
# CONSTANTS
#-------------------------------------------------

AUTHORS = [
    'Philip Arvidsson <contact@philiparvidsson.com>',
    'Mattias Eriksson <pls enter mail>'
]

VERSION = '0.1'

#-------------------------------------------------
# CLASSES
#-------------------------------------------------

class Config(object):
    def __init__(self, opts):
        self.options = {
            # FIXME: Pick default target depending on platform. When we have bash, heh.
            '--target': 'bat'
        }

        for opt in opts:
            i = opt.find('=')
            if i >= 0:
                key   = opt[:i]
                value = opt[i+1:]
            else:
                key   = opt
                value = True

            self.options[key] = value

    def flag(self, s):
        return s in self.options

    def option(self, s):
        if s not in self.options:
            return False

        return self.options[s]

#-------------------------------------------------
# FUNCTIONS
#-------------------------------------------------

def compile_(tree):
    if config.option('--target') == 'bat':
        codegen = Batch(tree)
    else:
        # FIXME: Generate error here.
        pass

    codegen.generate_code()
    code = codegen.code()

    with open(config.destfile, 'w') as f:
        f.write(code)

def print_logo():
    print (
'''
smaragd v{}\n\ndevs: {}
'''.format(VERSION, '\n      '.join(AUTHORS))
)

def print_usage():
    print (
'''
Usage: smaragd [options] <srcfile> [destfile]

Options:
  --no-logo\t- don't display logo
  --no-optim\t- don't optimize
  --viz-ast\t- shows the syntax tree
'''
)

def viz_ast(root):
    visualize_ast(root)

#-------------------------------------------------
# SCRIPT
#-------------------------------------------------

if __name__ == '__main__':
    opts = filter(lambda s: s.startswith('--'), sys.argv)
    config = Config(opts)

    if not config.flag('--no-logo'):
        print_logo()

    if len(sys.argv) < 2:
        print_usage()
        sys.exit()

    config.srcfile  = sys.argv[-1]
    config.destfile = config.srcfile + '.bat'

    with open(config.srcfile, 'r') as f:
        source = StringSource(f.read())

    lexer  = Lexer(source)
    parser = Parser(lexer)

    tree = parser.generate_ast()

    if not config.flag('--no-optim'):
        optim = ASTOptimizer()
        optim.optimize_ast(tree)

    if config.flag('--viz-ast'):
        viz_ast(tree)
    else:
        compile_(tree)
