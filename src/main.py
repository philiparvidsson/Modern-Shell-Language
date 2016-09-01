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

    for token in token_list.tokens:
        print str(token)

    print "-" * 10

    bat = transpiler.Bat()
    while len(token_list.tokens) > 0:
        ast = lexer.generate_ast(token_list)
        print str(ast)
        transpiler.generate_code(bat, ast)

    print bat.code

#-------------------------------------------------
# SCRIPT
#-------------------------------------------------

if __name__=="__main__":
    transpile("../examples/test.mb")
