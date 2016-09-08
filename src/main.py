#-------------------------------------------------
# IMPORTS
#-------------------------------------------------

import os
import sys

import smaragd

from codegen.batch.batchgen import Batch
from debug.ast              import visualize_ast
from lexing.lexer           import Lexer
from lexing.source          import StringSource
from optim.astoptim         import ASTOptimizer
from parsing.parser         import Parser

#-------------------------------------------------
# FUNCTIONS
#-------------------------------------------------

def compile_(tree):
    if smaragd.conf.option('--target') == 'bat':
        codegen = Batch(tree)
    else:
        # FIXME: Generate error here.
        pass

    codegen.generate_code()
    code = codegen.code()

    with open(smaragd.conf.destfile, 'w') as f:
        f.write(code)

def print_logo():
    print (
'''
smaragd v{}\n\ndevs: {}
'''.format(smaragd.VERSION, '\n      '.join(smaragd.AUTHORS))
)

def print_usage():
    print (
'''
Usage: smaragd [options] <srcfile> [destfile]

Options:
  --max-errors=<n>\t- sets the max number of errors before exiting
  --no-logo\t\t- don't display logo
  --no-optim\t\t- don't optimize
  --viz-ast\t\t- shows the syntax tree
'''
)

def viz_ast(root):
    visualize_ast(root)

def main():
    opts = filter(lambda s: s.startswith('--'), sys.argv)
    smaragd.conf = smaragd.Config(opts)

    if not smaragd.conf.flag('--no-logo'):
        print_logo()

    if len(sys.argv) < 2:
        print_usage()
        sys.exit()

    smaragd.conf.srcfile  = sys.argv[-1]
    smaragd.conf.destfile = smaragd.conf.srcfile + '.bat'

    if not os.path.isfile(smaragd.conf.srcfile):
        fatal('no such file exists: {}'.format(smaragd.conf.srcfile))

    os.chdir(os.path.dirname(os.path.abspath(smaragd.conf.srcfile)))

    with open(smaragd.conf.srcfile, 'r') as f:
        source = StringSource(f.read())

    lexer  = Lexer(source)
    parser = Parser(lexer)

    tree = parser.generate_ast()

    if not smaragd.conf.flag('--no-optim'):
        optim = ASTOptimizer()
        optim.optimize_ast(tree)

    if smaragd.conf.flag('--viz-ast'):
        viz_ast(tree)
    else:
        compile_(tree)

#-------------------------------------------------
# SCRIPT
#-------------------------------------------------

if __name__ == '__main__':
    main()
