# Alpha-Beta Pruning Algorithm

## Aim

To implement the Alpha-Beta Pruning Algorithm and find the optimal move in a game tree while reducing the number of nodes that need to be evaluated.

---

# Introduction

Alpha-Beta Pruning is an improvement over the Minimax Algorithm. In Minimax, every node in the game tree is explored, which can take a lot of time when the tree becomes large. Alpha-Beta Pruning helps solve this problem by skipping some branches that cannot affect the final decision.

In simple words, if we already know that a particular branch will not give a better result than the current best option, there is no need to explore it further. This process is called **pruning**.

The final answer obtained by Alpha-Beta Pruning is exactly the same as Minimax, but usually with much less computation.

---

# Theory

Alpha-Beta Pruning uses two values:

### Alpha (α)

Alpha represents the best value that the MAX player can guarantee so far.

Initially,

```text
α = -∞
```

---

### Beta (β)

Beta represents the best value that the MIN player can guarantee so far.

Initially,

```text
β = +∞
```

---

### Pruning Condition

A branch can be pruned whenever:

```text
α ≥ β
```

At this point further exploration is useless because it cannot improve the final decision.

---

# Working Example

Consider the following game tree:

```text
                         MAX
                       /     \
                    MIN       MIN
                  /   \      /   \
                 3     5    2     9
```

---

### Evaluate Left MIN Node

```text
MIN(3,5)=3
```

Current Alpha:

```text
α = 3
```

---

### Evaluate Right MIN Node

First child:

```text
2
```

Current Beta:

```text
β = 2
```

Since

```text
β ≤ α

2 ≤ 3
```

the remaining branch containing value 9 is not explored.

Therefore it gets pruned.

---

Tree after pruning:

```text
                         MAX
                       /     \
                      3      2
```

---

Root Node:

```text
MAX(3,2)=3
```

Final Answer:

```text
Optimal Value = 3
```

---

# Algorithm

```text
ALPHA-BETA(node, depth, α, β, maximizing)

1. If node is terminal
      return node value

2. If maximizing player

      value = -∞

      For each child

            value = max(value,
                        AlphaBeta(child))

            α = max(α, value)

            If α ≥ β
                  break

      return value

3. Else

      value = +∞

      For each child

            value = min(value,
                        AlphaBeta(child))

            β = min(β, value)

            If β ≤ α
                  break

      return value
```

---

# Python Implementation

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
    """

    if depth == 0 or len(node.children) == 0:
        return node.value

    # MAX Player
    if is_maximizing:

        value = float('-inf')

        for child in node.children:

            value = max(
                value,
                alpha_beta(
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
                alpha_beta(
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
```

---

# Test Case 1

## Input Tree

```text
                         MAX
                       /     \
                    MIN       MIN
                  /   \      /   \
                 3     5    2     9
```

---

## Working

Left MIN Node:

```text
MIN(3,5)=3
```

Current Alpha:

```text
α = 3
```

---

Right MIN Node:

First child:

```text
2
```

Current Beta:

```text
β = 2
```

Since

```text
β ≤ α

2 ≤ 3
```

the node containing value 9 is pruned.

---

Root Node:

```text
MAX(3,2)=3
```

---

## Expected Output

```text
Optimal Value = 3
```

---

## Obtained Output

```text
Optimal Value = 3
```

---

## Result

The obtained output matches the expected output. One branch was successfully pruned, reducing the amount of search required.

---

# Test Case 2

## Input Tree

```text
                              MAX
                           /        \
                        MIN          MIN
                      /    \       /    \
                    10      7     5      8
```

---

## Working

Left MIN Node:

```text
MIN(10,7)=7
```

Current Alpha:

```text
α = 7
```

---

Right MIN Node:

First child:

```text
5
```

Current Beta:

```text
β = 5
```

Since

```text
β ≤ α

5 ≤ 7
```

the branch containing value 8 is pruned.

---

Root Node:

```text
MAX(7,5)=7
```

---

## Expected Output

```text
Optimal Value = 7
```

---

## Obtained Output

```text
Optimal Value = 7
```

---

## Result

The algorithm successfully produced the correct answer while avoiding unnecessary node exploration.

---

# Correctness of the Algorithm

The Alpha-Beta algorithm does not change the result obtained by Minimax. It only avoids evaluating branches that can never influence the final decision.

Because of this:

* Every important node is evaluated.
* Irrelevant branches are ignored.
* The final answer remains optimal.

Therefore the algorithm always produces the same result as Minimax while performing fewer computations.

---

# Complexity Analysis

Let:

* **b** = Branching Factor
* **d** = Depth of Tree

### Worst Case

When no pruning occurs:

[
O(b^d)
]

This is the same as Minimax.

---

### Best Case

When maximum pruning occurs:

[
O(b^{d/2})
]

This is much faster than Minimax.

---

### Space Complexity

[
O(d)
]

The recursive function calls are stored in the stack.

---

# Advantages

1. Produces the same result as Minimax.
2. Reduces the number of nodes explored.
3. Faster than Minimax in most situations.
4. Works well for large game trees.

---

# Limitations

1. Performance depends on node ordering.
2. Worst-case complexity is still similar to Minimax.
3. Can become expensive for very deep game trees.

---

# Conclusion

In this experiment, the Alpha-Beta Pruning algorithm was implemented and studied. The algorithm successfully returned the same optimal result as Minimax while exploring fewer nodes. The test cases showed how pruning eliminates unnecessary branches and improves efficiency. Because of this, Alpha-Beta Pruning is generally preferred over the basic Minimax algorithm for game-playing applications.
