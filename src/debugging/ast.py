#--------------------------------------------------
# FUNCTIONS
#--------------------------------------------------

def print_node(node, level):
    """Prints the specified node by displaying its information."""

    words = node.construct.split(' ')
    label = '_'.join([x[:4] for x in words])

    nodetype = node.construct
    tab = '    ' * (level-1)
    sep = '+-- ' if level > 0 else ''

    if node.data is not None:
        print tab + sep + '[{}: {}]'.format(nodetype, node.data)
    else:
        print tab + sep + '[{}]'.format(nodetype)

def visualize(root, level=0):
    """
    Visualizes the tree by drawing it with ASCII.
    :param root: The root node to visualize the tree from.
    :param level: Reserved.
    """

    print_node(root, level)

    if root.children:
        for child in root.children:
            visualize(child, level+1)
