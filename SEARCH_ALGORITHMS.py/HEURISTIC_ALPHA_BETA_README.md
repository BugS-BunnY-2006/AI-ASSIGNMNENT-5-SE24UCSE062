## Heuristic Alpha-Beta Search

## Aim

To implement the Heuristic Alpha-Beta Search Algorithm and find the best possible move when it is not practical to search the entire game tree.

---

# Introduction

In many real-world games such as Chess, the game tree can become extremely large. Even though Alpha-Beta Pruning reduces the number of nodes explored, searching the complete tree is still not possible in many situations.

To overcome this problem, a depth limit is introduced. When the depth limit is reached, instead of continuing the search, the algorithm estimates how good the current position is using a **heuristic evaluation function**.

Because of this, the algorithm can make decisions much faster while still producing reasonably good results.

---

# Theory

A heuristic is basically an educated guess. Instead of finding the exact answer by exploring all future moves, the algorithm estimates the quality of a position.

For example in Chess:

```text
Evaluation Score =
(Number of White Pieces)
-
(Number of Black Pieces)
```

A positive score indicates a better position for MAX.

A negative score indicates a better position for MIN.

---

### Heuristic Evaluation Function

A simple heuristic function can be written as:

```text
Heuristic Value =
Player Score - Opponent Score
```

This value is returned whenever the specified depth limit is reached.

---

# Working Example

Suppose the search depth is limited to 2 levels.

```text
                            MAX
                          /      \
                        MIN       MIN
                      /    \     /    \
                     5      8   4      6
```

Since depth limit is reached, these values are treated as heuristic scores.

MIN nodes:

```text
MIN(5,8)=5

MIN(4,6)=4
```

MAX node:

```text
MAX(5,4)=5
```

Final Answer:

```text
Best Value = 5
```

---

# Algorithm

```text
HEURISTIC_ALPHA_BETA
(Node, Depth, Alpha, Beta, Maximizing)

1. If Depth = 0
      Return Heuristic(Node)

2. If Node is Terminal
      Return Node Value

3. If Maximizing

      Value = -∞

      For each Child

            Value = max(Value,
                        Recursive Call)

            Alpha = max(Alpha, Value)

            If Alpha ≥ Beta
                  Break

      Return Value

4. Else

      Value = +∞

      For each Child

            Value = min(Value,
                        Recursive Call)

            Beta = min(Beta, Value)

            If Beta ≤ Alpha
                  Break

      Return Value
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


def heuristic(node):
    """
    Heuristic Evaluation Function
    """

    return node.value


def heuristic_alpha_beta(node,
                         depth,
                         alpha,
                         beta,
                         is_maximizing):

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
```

---

# Test Case 1

## Input Tree

```text
                           MAX
                         /      \
                       MIN       MIN
                     /    \     /    \
                    5      8   4      6
```

---

## Working

Left MIN Node:

```text
MIN(5,8)=5
```

Right MIN Node:

```text
MIN(4,6)=4
```

Root MAX Node:

```text
MAX(5,4)=5
```

---

## Expected Output

```text
Best Value = 5
```

---

## Obtained Output

```text
Best Value = 5
```

---

## Result

The output matches the expected result. Therefore the algorithm works correctly for this test case.

---

# Test Case 2

## Input Tree

```text
                           MAX
                         /      \
                       MIN       MIN
                     /    \     /    \
                    7      3   10      4
```

---

## Working

Left MIN Node:

```text
MIN(7,3)=3
```

Right MIN Node:

```text
MIN(10,4)=4
```

Root MAX Node:

```text
MAX(3,4)=4
```

---

## Expected Output

```text
Best Value = 4
```

---

## Obtained Output

```text
Best Value = 4
```

---

## Result

The obtained result is same as the expected result, showing that the implementation works properly.

---

# Correctness of the Algorithm

The algorithm combines Alpha-Beta Pruning with heuristic evaluation. Whenever the search reaches the specified depth limit, the heuristic function estimates the quality of that position. The pruning mechanism further reduces unnecessary exploration.

Although the result may not always be perfectly optimal due to the depth limit, it usually provides a very good approximation while significantly reducing computation time.

---

# Complexity Analysis

Let:

* **b** = Branching Factor
* **d** = Search Depth

### Time Complexity

Worst Case:

[
O(b^d)
]

Best Case:

[
O(b^{d/2})
]

---

### Space Complexity

[
O(d)
]

---

# Advantages

1. Faster than full Alpha-Beta Search.
2. Suitable for large game trees.
3. Reduces computation time significantly.
4. Can be applied to real-world games such as Chess.

---

# Limitations

1. Result depends on the quality of the heuristic function.
2. May not always produce the exact optimal move.
3. Poor heuristics can lead to poor decisions.

---

# Conclusion

In this experiment, Heuristic Alpha-Beta Search was implemented successfully. By introducing a heuristic evaluation function and limiting the search depth, the algorithm was able to make decisions much faster than a complete search. The test cases verified the correctness of the implementation, and the results demonstrated the usefulness of heuristic-based search in large game environments.

