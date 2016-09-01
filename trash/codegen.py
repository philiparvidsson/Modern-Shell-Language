#-------------------------------------------------
# IMPORTS
#-------------------------------------------------

import ast

#-------------------------------------------------
# FUNCTIONS
#-------------------------------------------------

def gen_assign(node):
    #
    #          ASSIGN
    #            /\
    #           /  \
    #          /    \
    # IDENTIFIER     EXPR
    #
    ident = node.children[0]
    expr  = node.children[1]

def gen_code(node):
    # Generate batch code here
    if node.kind == ast.Node.ASSIGN:
        gen_assign(node)
