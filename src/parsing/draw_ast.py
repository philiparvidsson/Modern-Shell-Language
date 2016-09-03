#--------------------------------------------------
# HELPERS
#--------------------------------------------------

def print_node(node, level):
    words = node.construct.split(' ')
    s = '_'.join([x[:4] for x in words])

    nodetype = s# node.construct[0:3]
    tab = "    " * (level - 1)
    sep = "|-- " if level > 0 else ""

    if node.data:
        print(tab + sep + "[{}: {}]".format(nodetype, node.data))
    else:
        print(tab + sep + "[{}]".format(nodetype))

def visualize(node, level=0):
    print_node(node, level)

    if node.children:
        for child in node.children:
            visualize(child, level+1)

def draw_ast_tree(node):
    print("\n---AST-----------------------------------")
    visualize(node)
    print("-----------------------------------------\n")
