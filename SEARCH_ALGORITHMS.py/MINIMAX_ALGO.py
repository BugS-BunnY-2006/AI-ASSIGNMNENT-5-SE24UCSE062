class Node:
    """
    Represents a node in the game tree.
    Each node may contain a value and child nodes.
    """

    def __init__(self, value=None):
        self.value = value
        self.children = []

    def add_child(self, child):
        """
        Adds a child node to the current node.
        """
        self.children.append(child)


def minimax(node, is_maximizing):
    """
    Minimax Algorithm

    Parameters:
        node            : Current node in the game tree
        is_maximizing   : True if MAX player's turn,
                          False if MIN player's turn

    Returns:
        Optimal value for the current node
    """

    # Base Case
    if len(node.children) == 0:
        return node.value

    # MAX Player
    if is_maximizing:

        best_value = float('-inf')

        for child in node.children:
            value = minimax(child, False)
            best_value = max(best_value, value)

        return best_value

    # MIN Player
    else:

        best_value = float('inf')

        for child in node.children:
            value = minimax(child, True)
            best_value = min(best_value, value)

        return best_value
