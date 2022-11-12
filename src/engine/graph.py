"""
Solve the knapsack problem via graph theory

Items have weights (integers) and values
Which items do we take to maximise value while being under a threshold weight?

"""

from dataclasses import dataclass
import graphviz

dot = graphviz.Digraph(comment="scran graph")


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

    def __init__(self, current_weight: int, item_considered: Item):
        self.current_weight: int = current_weight
        self.item_considered: Item = item_considered

        dot.node(
            f"{self.item_considered.label}",
            f"{self.item_considered.label}, {self.current_weight}",
        )

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
        """ Add edge to the graph """

        edge = Edge(next, -1 * value)

        if edge not in (edges := self.adj_list[current.item_considered]):
            edges.append(edge)
            dot.edge(f"{current.item_considered.label}", f"{next.item_considered.label}", f"{-1 * value}")
        else:
            print(f'Edge {edge} already exists')

    def neighbours(self, node: Node) -> list[Node]:
        """ return the neighbours of a node """
        edge: Edge
        return [edge.next_node for edge in self.adj_list[node.item_considered]]

    def edges_from(self, node: Node) -> list[Edge]:
        """ return list of edges from a node"""
        return [edge for edge in self.adj_list[node.item_considered]]

