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
