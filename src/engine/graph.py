"""
Solve the knapsack problem via graph theory

Items have weights (integers) and values
Which items do we take to maximise value while being under a threshold weight?

"""

from dataclasses import dataclass


@dataclass
class Item:
    """Items being considered"""

    label: str
    weight: int
    value: int

    def __hash__(self):
        return hash(f"{self.label}, {self.weight}, {self.value}")


@dataclass
class Node:
    """Nodes that store state; tracks current value of knapsack
    and item being considered"""

    current_weight: int
    item_considered: Item

    def __hash__(self):
        return hash(f"{self.current_weight}, {self.item_considered}")


@dataclass
class Edge:
    next_node: Node
    value: int


class Graph:
    """Adjacency list representation of digraph
    Can only go forward along digraph (cannot traverse backwards)"""

    def __init__(self, items: list[Item], capacity: int):
        self.items = items  # list of items that need consideration
        self.capacity = capacity

        # initialise empty adjacency list
        self.adj_list: dict[Item, list[Edge]] = {item: [] for item in items}

    def add_edge(self, current: Node, next: Node, value: int) -> None:
        """Add edge to the graph"""
        self.adj_list[current.item_considered].append(Edge(next, value))
