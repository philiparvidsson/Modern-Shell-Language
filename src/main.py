#-------------------------------------------------
# IMPORTS
#-------------------------------------------------

from crutch import parser

#-------------------------------------------------
# FUNCTIONS
#-------------------------------------------------

def transpile(file_name):
    file = open(file_name);
    source_code = file.read()
    file.close()

    tokens = parser.parse_into_tokens(source_code)

    for token in tokens:
        print str(token)

#-------------------------------------------------
# SCRIPT
#-------------------------------------------------

if __name__=="__main__":
    transpile("../examples/test.mb")
