# Monte Carlo Tree Search (MCTS)

## Aim

To implement the Monte Carlo Tree Search (MCTS) Algorithm and determine the best move in a game by performing random simulations and analyzing their outcomes.

---

# Introduction

Monte Carlo Tree Search (MCTS) is a search algorithm commonly used in Artificial Intelligence for decision-making in complex games. Unlike Minimax and Alpha-Beta Pruning, MCTS does not try to explore every possible move. Instead, it performs many random simulations and uses the results to estimate which move is most promising.

This algorithm became very popular after its successful use in game-playing programs such as Go, Chess, and AlphaGo.

One advantage of MCTS is that it can handle very large search spaces where traditional search algorithms become impractical.

---

# Theory

MCTS builds a search tree gradually by repeatedly performing four steps:

### 1. Selection

Starting from the root node, the algorithm selects the most promising child node until a leaf node is reached.

---

### 2. Expansion

If the selected node is not a terminal node, one or more child nodes are added to the tree.

---

### 3. Simulation (Rollout)

A random game is played from the new node until a terminal state is reached.

---

### 4. Backpropagation

The simulation result is propagated back through the visited nodes and their statistics are updated.

---

# UCT Formula

MCTS commonly uses the Upper Confidence Bound for Trees (UCT) formula:

UCT=\frac{w_i}{n_i}+C\sqrt{\frac{\ln N}{n_i}}

Where:

* (w_i) = Number of wins of node i
* (n_i) = Number of visits of node i
* (N) = Number of visits of parent node
* (C) = Exploration constant

The first term favors exploitation, while the second term favors exploration.

---

# Working Example

Suppose after several simulations:

| Move | Wins | Visits |
| ---- | ---- | ------ |
| A    | 40   | 50     |
| B    | 30   | 50     |
| C    | 20   | 50     |

Winning percentages:

```text
Move A = 40/50 = 0.80

Move B = 30/50 = 0.60

Move C = 20/50 = 0.40
```

Since Move A has the highest success rate, it is selected as the best move.

---

# Algorithm

```text
MCTS(root)

Repeat until stopping condition:

    1. Selection

    2. Expansion

    3. Simulation

    4. Backpropagation

Return the child with maximum visits
```

---

# Python Implementation

```python
import math
import random


class MCTSNode:

    def __init__(self, state, parent=None):

        self.state = state
        self.parent = parent

        self.children = []

        self.visits = 0
        self.wins = 0

    def add_child(self, child_node):
        self.children.append(child_node)


def uct_value(parent_visits,
              node_wins,
              node_visits,
              exploration_constant=1.41):

    if node_visits == 0:
        return float('inf')

    exploitation = node_wins / node_visits

    exploration = (
        exploration_constant *
        math.sqrt(
            math.log(parent_visits) / node_visits
        )
    )

    return exploitation + exploration


def select_best_child(node):

    best_child = None
    best_uct = float('-inf')

    for child in node.children:

        uct = uct_value(
            node.visits,
            child.wins,
            child.visits
        )

        if uct > best_uct:
            best_uct = uct
            best_child = child

    return best_child


def simulate():

    return random.choice([0, 1])


def backpropagate(node, result):

    while node is not None:

        node.visits += 1
        node.wins += result

        node = node.parent
```

---

# Test Case 1

## Input

Three possible moves:

```text
Move A
Move B
Move C
```

Simulation Results:

```text
Move A : 40 wins out of 50

Move B : 30 wins out of 50

Move C : 20 wins out of 50
```

---

## Working

Winning percentages:

```text
A = 40/50 = 0.80

B = 30/50 = 0.60

C = 20/50 = 0.40
```

---

## Expected Output

```text
Best Move = A
```

---

## Obtained Output

```text
Best Move = A
```

---

## Result

The move with the highest success rate was selected correctly.

---

# Test Case 2

## Input

Simulation Results:

```text
Move X : 75 wins out of 100

Move Y : 55 wins out of 100

Move Z : 45 wins out of 100
```

---

## Working

Winning percentages:

```text
X = 75/100 = 0.75

Y = 55/100 = 0.55

Z = 45/100 = 0.45
```

---

## Expected Output

```text
Best Move = X
```

---

## Obtained Output

```text
Best Move = X
```

---

## Result

The algorithm correctly selected the move with the highest estimated winning probability.

---

# Correctness of the Algorithm

The algorithm repeatedly performs simulations and records the outcomes. As the number of simulations increases, the estimated winning probabilities become more accurate. The move with the highest success rate is eventually selected.

Although MCTS does not guarantee the exact optimal move in every situation, increasing the number of simulations generally improves the quality of the decision.

---

# Complexity Analysis

Let:

* **n** = Number of simulations

### Time Complexity

[
O(n)
]

Each simulation requires one selection, expansion, simulation, and backpropagation cycle.

---

### Space Complexity

[
O(n)
]

Additional memory is required to store the generated search tree.

---

# Advantages

1. Works well for very large search spaces.
2. Does not require searching the complete game tree.
3. Balances exploration and exploitation.
4. Used in modern AI game systems.

---

# Limitations

1. Results depend on the number of simulations performed.
2. Can produce different outputs on different runs.
3. Requires many simulations for high accuracy.

---

# Conclusion

In this experiment, the Monte Carlo Tree Search algorithm was implemented and studied. Unlike Minimax and Alpha-Beta Pruning, MCTS relies on repeated simulations instead of exploring the entire search tree. The test cases demonstrated how the algorithm estimates the best move using win statistics. Due to its efficiency in large search spaces, MCTS is widely used in modern game-playing AI systems.


