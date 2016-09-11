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

def parse_file(s):
    with open(s, 'r') as f:
        source = StringSource(f.read())

    lexer  = Lexer(source)
    parser = Parser(lexer)

    if smaragd.num_errors > 0:
        smaragd.fatal('there were errors')

    tree = parser.generate_ast()

    if not smaragd.conf.flag('--no-optim'):
        optim = ASTOptimizer()
        optim.optimize_ast(tree)

    analyzer = SemanticAnalyzer()
    analyzer.verify(tree)

    if smaragd.num_errors > 0:
        smaragd.fatal('there were errors')

    return tree

def compile_(tree, destfile):
    target = smaragd.conf.option('--target')
    if target == 'bat':
        codegen = Batch(tree)
    else:
        # FIXME: Generate error here.
        smaragd.fatal('unsupported target'.format(target))

    #smaragd.trace('generating code...')

    codegen.generate_code()
    code = codegen.code()

    with open(destfile, 'w') as f:
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
  --analyze         - only perform semantic analysis
  --max-errors=<n>  - set the max number of errors before exiting
  --no-logo         - don't display logo
  --no-optim        - don't optimize
  --no-warn         - suppress warnings
  --show-ast        - show abstract syntax tree
  --target=<s>      - compile to the specified target ('bat')
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

    srcfile  = sys.argv[-1]
    destfile = srcfile + '.bat'

    if not os.path.isfile(srcfile):
        smaragd.fatal('no such file')

    #os.chdir(os.path.dirname(os.path.abspath(smaragd.conf.srcfile)))

    #smaragd.trace('generating syntax tree...')
    tree = parse_file(srcfile)

    if smaragd.conf.flag('--show-ast'):
        show_ast(tree)
    elif not smaragd.conf.flag('--analyze'):
        # Semantic analysis is really only relevant for code generation.
        compile_(tree, destfile)

#-------------------------------------------------
# SCRIPT
#-------------------------------------------------

if __name__ == '__main__':
    main()
