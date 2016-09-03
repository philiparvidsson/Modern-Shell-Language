#--------------------------------------------------
# HELPERS
#--------------------------------------------------

def print_node(node, level):
    nodetype = node.construct[0:3]
    tab = "    " * (level - 1)
    sep = "|-- " if level > 0 else ""

    print(tab + sep + "[{}: {}]".format(nodetype, node.data))

def visualize(node, level=0):
    print_node(node)
    for child in node.children:
        visualize(child, level+1)

def draw_ast_tree(node):
    print("\n---AST-----------------------------------")
    visualize(node)
    print("-----------------------------------------\n")