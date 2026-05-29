# 2. Alpha-Beta Pruning Algorithm – Implementation Code

```python
class Node:
    """
    Represents a node in the game tree.
    """

    def __init__(self, value=None):
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)


def alpha_beta(node, depth, alpha, beta, is_maximizing):
    """
    Alpha-Beta Pruning Algorithm

    Parameters:
        node           : Current node
        depth          : Depth of search tree
        alpha          : Best value for MAX
        beta           : Best value for MIN
        is_maximizing  : True for MAX player,
                         False for MIN player

    Returns:
        Optimal value after pruning
    """

    # Terminal Node or Depth Limit Reached
    if depth == 0 or len(node.children) == 0:
        return node.value

    # MAX Player
    if is_maximizing:

        value = float('-inf')

        for child in node.children:

            value = max(
                value,
                alpha_beta(child,
                           depth - 1,
                           alpha,
                           beta,
                           False)
            )

            alpha = max(alpha, value)

            # Pruning Condition
            if alpha >= beta:
                break

        return value

    # MIN Player
    else:

        value = float('inf')

        for child in node.children:

            value = min(
                value,
                alpha_beta(child,
                           depth - 1,
                           alpha,
                           beta,
                           True)
            )

            beta = min(beta, value)

            # Pruning Condition
            if beta <= alpha:
                break

        return value
```

