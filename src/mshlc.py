#-------------------------------------------------
# IMPORTS
#-------------------------------------------------

import os
import sys

import mshl

from codegen.batch.batchgen import Batch
from debug.ast              import visualize_ast
from lexing.lexer           import Lexer
from lexing.source          import StringSource
from optimize.astoptimizer  import ASTOptimizer
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

    if mshl.num_errors > 0:
        mshl.fatal('there were errors')

    tree = parser.generate_ast()

    if not mshl.conf.flag('--no-optim'):
        optim = ASTOptimizer()
        optim.optimize_ast(tree)

    analyzer = SemanticAnalyzer()
    analyzer.verify(tree)

    if mshl.num_errors > 0:
        mshl.fatal('there were errors')

    return tree

def compile_(tree, destfile):
    target = mshl.conf.option('--target')
    if target == 'bat':
        codegen = Batch(tree)
    else:
        # FIXME: Generate error here.
        mshl.fatal('unsupported target'.format(target))

    #mshl.trace('generating code...')

    codegen.generate_code()
    code = codegen.code()

    if mshl.conf.option('--show-code'):
        mshl.trace(code)
    else:
        with open(destfile, 'w') as f:
            f.write(code)

def print_logo():
    print (
'''
mshlc v{}\n\ndevs: {}
'''.format(mshl.VERSION, '\n      '.join(mshl.AUTHORS))
)

def print_usage():
    print (
'''
Usage: mshlc [options] <srcfile> [destfile]

Options:
  --analyze         - only perform semantic analysis
  --inc-dir=<s>     - adds a path as an include directory
  --max-errors=<n>  - set the max number of errors before exiting
  --no-logo         - don't display logo
  --no-optim        - don't optimize
  --no-warn         - suppress warnings
  --show-ast        - show abstract syntax tree
  --show-code       - show code (do not write to file)
  --target=<s>      - compile to the specified target ('bat')
  --warn-err        - treat warnings as errors
'''
)

def show_ast(root):
    print
    visualize_ast(root)

def main():
    opts = filter(lambda s: s.startswith('--'), sys.argv)
    mshl.conf = mshl.Config(opts)

    if not mshl.conf.flag('--no-logo'):
        print_logo()

    if len(sys.argv) < 2:
        print_usage()
        sys.exit()

    mshl.srcfile  = sys.argv[-1]
    destfile = mshl.srcfile + '.bat'

    if not os.path.isfile(mshl.srcfile):
        mshl.fatal('no such file')

    #os.chdir(os.path.dirname(os.path.abspath(mshl.conf.mshl.srcfile)))

    #mshl.trace('generating syntax tree...')
    tree = parse_file(mshl.srcfile)

    if mshl.conf.flag('--show-ast'):
        show_ast(tree)
    elif not mshl.conf.flag('--analyze'):
        # Semantic analysis is really only relevant for code generation.
        compile_(tree, destfile)

#-------------------------------------------------
# SCRIPT
#-------------------------------------------------

if __name__ == '__main__':
    main()
