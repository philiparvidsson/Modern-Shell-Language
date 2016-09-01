import ast
import parse

def transpile(file_name):
    file = open(file_name);
    source_code = file.read()
    file.close()

    tokens = parse.into_tokens(source_code)

    for token in tokens:
        print str(token)

    tree = ast.from_tokens(tokens)
    print str(tree)

if __name__=="__main__":
    transpile("../examples/test.mb")
