"""
Solve the knapsack problem via graph theory

Items have weights (integers) and values
Which items do we take to maximise value while being under a threshold weight?

"""
from dataclasses import dataclass, field
import graphviz

dot = graphviz.Digraph(comment="scran graph")


class EdgeDoesNotExistException(Exception):
    """Edge does not exist"""


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
            f"{self.item_considered.label}{self.current_weight}",
            f"{self.item_considered.label}, {self.current_weight}",
        )

    def __hash__(self):
        return hash(f"{self.current_weight}, {self.item_considered}")

    def __repr__(self):
        return f"Node({self.current_weight}, {self.item_considered})"


@dataclass
class Edge:
    next_node: Node
    value: int


@dataclass
class Queue:
    """For use with nodes or edges"""

    _queue: list = field(default_factory=lambda: [])  # type: ignore

    def enqueue(self, item: Edge | Node) -> None:
        self._queue.append(item)

    def dequeue(self) -> Edge | Node:
        return self._queue.pop(0)

    def __bool__(self):
        return bool(self._queue)


class Graph:
    """Adjacency list representation of digraph
    Can only go forward along digraph (cannot traverse backwards)"""

    def __init__(self, items: list[Item] | None = None):

        if items:
            self.items: list[Item] = items  # list of items that need consideration
        else:
            self.items: list[Item] = []

        # initialise empty adjacency list
        self.adj_list: dict[Item, list[Edge]] = (
            {item: [] for item in items} if items else {}
        )

    def add_edge(self, current: Node, next: Node, value: int) -> None:
        """Add edge to the graph"""

        edge = Edge(next, -1 * value)

        edges = self.adj_list[current.item_considered]
        edges.append(edge)
        dot.edge(
            f"{current.item_considered.label}{current.current_weight}",
            f"{next.item_considered.label}{next.current_weight}",
            f"{-1 * value}",
        )

    def neighbours(self, node: Node) -> list[Node]:
        """return the neighbours of a node"""
        edge: Edge
        return [edge.next_node for edge in self.adj_list[node.item_considered]]

    def edges_from(self, node: Node) -> list[Edge]:
        """return list of edges from a node"""
        return [edge for edge in self.adj_list[node.item_considered]]

    def add_node(self, node: Node):
        """Adds node to graph with no edges"""
        self.adj_list[node.item_considered] = []

    def node_exists(self, node: Node):
        return True if node.item_considered in self.adj_list.keys() else False

    def is_edge(self, src_node: Node, dest_node: Node) -> int:
        """checks for edge between nodes s and d.
        directional - given s->d, is_edge(s, d) returns True but is_edge(d, s)
        returns False"""

        return (
            True
            if dest_node.item_considered
            in [
                edge.next_node.item_considered
                for edge in self.adj_list[src_node.item_considered]
            ]
            else False
        )

    def edge_weight(self, src: Node, dest: Node):
        """returns the weight of an edge - raises error if it does not exist"""
        if not self.is_edge(src, dest):
            raise EdgeDoesNotExistException

        else:
            return -1 * dest.item_considered.value
