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
    while len(token_list.tokens) > 0:
        print '-' * 30
        for t in token_list.tokens:
            print t
        ast = lexer.generate_ast(token_list)
        print lexer.draw_ast_tree(ast)
        transpiler.generate_code(bat, ast)

    print
    print
    print bat.code

#-------------------------------------------------
# SCRIPT
#-------------------------------------------------

if __name__=="__main__":
    transpile("../examples/test.mb")
