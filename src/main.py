#-------------------------------------------------
# IMPORTS
#-------------------------------------------------

from crutch import codegen, lexer, parser

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

    ast = lexer.generate_ast(token_list)
    print str(ast)

    print "-" * 10

    codegen.generate_code(ast)

#-------------------------------------------------
# SCRIPT
#-------------------------------------------------

if __name__=="__main__":
    transpile("../examples/test.mb")
