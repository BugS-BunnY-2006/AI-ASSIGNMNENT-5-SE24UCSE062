# 1. Minimax Algorithm

## Aim

To implement the Minimax Algorithm and find the best possible move in a two-player game where one player tries to maximize the score and the other tries to minimize it.

---

# Introduction

Minimax is one of the most basic and important algorithms used in Artificial Intelligence for game playing. It is mainly used in two-player games such as Tic-Tac-Toe, Chess, Checkers, etc.

The idea behind this algorithm is pretty simple. One player (called MAX) tries to get the highest score possible, while the other player (called MIN) tries to reduce that score. The algorithm explores all possible moves and then chooses the move that gives the best result assuming that both players play perfectly.

Although Minimax guarantees the optimal move, it can become very slow when the game tree becomes large because it has to examine every possible state.

---

# Theory

The algorithm works recursively.

* MAX player always chooses the largest value.
* MIN player always chooses the smallest value.
* Values are propagated from the leaf nodes towards the root.
* The value obtained at the root node becomes the final decision.

For example, consider the following game tree:

```text
                    MAX
                  /     \
                MIN     MIN
               /  \     /  \
              3    5   2    9
```

### Evaluating MIN Nodes

For the left MIN node:

```text
MIN(3,5)=3
```

For the right MIN node:

```text
MIN(2,9)=2
```

Now the tree becomes:

```text
                    MAX
                  /     \
                 3       2
```

The MAX player chooses:

```text
MAX(3,2)=3
```

Therefore the optimal value is:

```text
3
```

---

# Algorithm

```text
MINIMAX(Node, MaximizingPlayer)

1. If the node is a leaf node
      return its value

2. If it is MAX player's turn

      best = -∞

      For each child node
            value = MINIMAX(child, False)

            best = max(best, value)

      return best

3. Else

      best = +∞

      For each child node
            value = MINIMAX(child, True)

            best = min(best, value)

      return best
```

---

# Python Implementation

```python
class Node:
    def __init__(self, value=None):
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)


def minimax(node, maximizing_player):

    # If it is a leaf node return the value

    if len(node.children) == 0:
        return node.value

    # MAX Player

    if maximizing_player:

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


# ----------------------------
# Test Case 1
# ----------------------------

root = Node()

left = Node()
right = Node()

root.add_child(left)
root.add_child(right)

left.add_child(Node(3))
left.add_child(Node(5))

right.add_child(Node(2))
right.add_child(Node(9))

result = minimax(root, True)

print("Optimal Value =", result)
```

---

# Test Case 1

## Input

```text
                    MAX
                  /     \
                MIN     MIN
               /  \     /  \
              3    5   2    9
```

## Working

First the MIN nodes are evaluated.

Left side:

```text
MIN(3,5)=3
```

Right side:

```text
MIN(2,9)=2
```

Then the root MAX node is evaluated.

```text
MAX(3,2)=3
```

## Expected Output

```text
Optimal Value = 3
```

## Obtained Output

```text
Optimal Value = 3
```

## Result

The output obtained is same as the expected output. Hence the algorithm works correctly for this test case.

---

# Test Case 2

## Code Changes

Only the leaf node values are changed.

```python
root = Node()

left = Node()
right = Node()

root.add_child(left)
root.add_child(right)

left.add_child(Node(10))
left.add_child(Node(7))

right.add_child(Node(5))
right.add_child(Node(8))

result = minimax(root, True)

print("Optimal Value =", result)
```

## Input

```text
                    MAX
                  /     \
                MIN     MIN
               /  \     /  \
             10    7   5    8
```

## Working

Left MIN node:

```text
MIN(10,7)=7
```

Right MIN node:

```text
MIN(5,8)=5
```

Root MAX node:

```text
MAX(7,5)=7
```

## Expected Output

```text
Optimal Value = 7
```

## Obtained Output

```text
Optimal Value = 7
```

## Result

The obtained result matches with the expected result. Therefore the implementation is correct for this test case also.

---

# Complexity Analysis

Let:

* **b** = branching factor
* **d** = depth of the tree

### Time Complexity

[
O(b^d)
]

This is because every possible node in the game tree is explored.

### Space Complexity

[
O(d)
]

The recursive function calls are stored in the stack, so the maximum space required depends on the depth of the tree.

---

# Advantages

1. Always gives the optimal move.
2. Concept is easy to understand.
3. Works well for small game trees.
4. Forms the base for many advanced game search algorithms.

---

# Limitations

1. It becomes slow when the depth increases.
2. A large amount of memory may be required.
3. Many unnecessary nodes are explored.
4. Not very practical for complex games without optimizations.

---

# Conclusion

In this implementation, the Minimax algorithm was successfully developed and tested on two different game trees. The outputs obtained matched the expected results in both cases. From the results it can be seen that the algorithm correctly chooses the best possible move assuming that both players make optimal decisions. Even though it is computationally expensive, it provides a good foundation for understanding game playing AI algorithms.


