#-------------------------------------------------
# IMPORTS
#-------------------------------------------------

from crutch import lexer, parser, transpiler

#-------------------------------------------------
# FUNCTIONS
#-------------------------------------------------

def transpile(file_name):
    file = open(file_name);
    source_code = file.read()
    file.close()

    token_list = parser.parse_into_tokens(source_code)

    bat = transpiler.Bat()
    roots = []
    funcs = []
    while len(token_list.tokens) > 0:
        print '-' * 30
        for t in token_list.tokens:
            print t
        ast = lexer.generate_ast(token_list)
        lexer.draw_ast_tree(ast)

        if ast.kind == lexer.FUNC:
            funcs.append(ast)
        else:
            roots.append(ast)

    for root in roots:
        transpiler.generate_code(bat, root)

    bat.finish()

    for root in funcs:
        transpiler.generate_code(bat, root)

    print
    print
    print bat.code

#-------------------------------------------------
# SCRIPT
#-------------------------------------------------

if __name__=="__main__":
    transpile("../examples/test.mb")
