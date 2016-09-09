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
from semantics.analyzer     import SemanticAnalyzer

#-------------------------------------------------
# FUNCTIONS
#-------------------------------------------------

def compile_(tree):
    target = smaragd.conf.option('--target')
    if target == 'bat':
        codegen = Batch(tree)
    else:
        # FIXME: Generate error here.
        smaragd.fatal('unsupported target'.format(target))

    smaragd.trace('generating code...')

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
  --max-errors=<n>  - sets the max number of errors before exiting
  --no-logo         - don't display logo
  --no-optim        - don't optimize
  --no-warn         - suppress warnings
  --show-ast        - shows the syntax tree
  --warn-err        - treat warnings as errors
'''
)

def show_ast(root):
    print
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
        smaragd.fatal('no such file exists')

    #smaragd.trace('source:', smaragd.conf.srcfile)
    #smaragd.trace('output:', smaragd.conf.destfile)
    #smaragd.trace()

    #os.chdir(os.path.dirname(os.path.abspath(smaragd.conf.srcfile)))

    with open(smaragd.conf.srcfile, 'r') as f:
        source = StringSource(f.read())

    lexer  = Lexer(source)
    parser = Parser(lexer)

    smaragd.trace('generating syntax tree...')
    tree = parser.generate_ast()

    if smaragd.conf.num_errors > 0:
        smaragd.fatal('there were errors')

    if not smaragd.conf.flag('--no-optim'):
        optim = ASTOptimizer()
        optim.optimize_ast(tree)

    if smaragd.conf.flag('--show-ast'):
        show_ast(tree)
    else:
        # Semantic analysis is really only relevant for code generation.
        analyzer = SemanticAnalyzer()
        analyzer.verify(tree)

        if smaragd.conf.num_errors > 0:
            smaragd.fatal('there were errors')

        compile_(tree)

    smaragd.trace()
    smaragd.trace('done.')

#-------------------------------------------------
# SCRIPT
#-------------------------------------------------

if __name__ == '__main__':
    main()
