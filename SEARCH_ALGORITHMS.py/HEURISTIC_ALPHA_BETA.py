class Node:
    """
    Represents a node in the game tree.
    """

    def __init__(self, value=None):
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)


def heuristic(node):
    """
    Heuristic evaluation function.
    Returns the estimated value of a node.
    """

    return node.value


def heuristic_alpha_beta(node,
                         depth,
                         alpha,
                         beta,
                         is_maximizing):
    """
    Heuristic Alpha-Beta Search Algorithm

    Parameters:
        node           : Current node
        depth          : Remaining search depth
        alpha          : Best value for MAX player
        beta           : Best value for MIN player
        is_maximizing  : True if MAX player's turn,
                         False if MIN player's turn

    Returns:
        Best estimated value
    """

    # Depth limit reached
    if depth == 0:
        return heuristic(node)

    # Terminal node
    if len(node.children) == 0:
        return node.value

    # MAX Player
    if is_maximizing:

        value = float('-inf')

        for child in node.children:

            value = max(
                value,
                heuristic_alpha_beta(
                    child,
                    depth - 1,
                    alpha,
                    beta,
                    False
                )
            )

            alpha = max(alpha, value)

            if alpha >= beta:
                break

        return value

    # MIN Player
    else:

        value = float('inf')

        for child in node.children:

            value = min(
                value,
                heuristic_alpha_beta(
                    child,
                    depth - 1,
                    alpha,
                    beta,
                    True
                )
            )

            beta = min(beta, value)

            if beta <= alpha:
                break

        return value
