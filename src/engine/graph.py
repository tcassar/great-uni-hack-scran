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

    def __str__(self):
        return f"{self.label}: w={self.weight}, v={self.value}"


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

    def __eq__(self, other):
        if f"{self.item_considered}{self.current_weight}" == f"{other.item_considered}{other.current_weight}":
            return True
        else:
            return False

    def __hash__(self):
        return hash(f"{self.current_weight}, {self.item_considered}")

    def __repr__(self):
        return f"Node({self.current_weight}, {self.item_considered})"

    def __str__(self):
        return f"{self.item_considered.label}, {self.current_weight}"


@dataclass
class Edge:
    next_node: Node
    value: int

    def __eq__(self, other):
        if f'{self.next_node}{self.value}' == f"{other.next_node}{other.value}":
            return True
        else:
            return False


@dataclass
class Queue:
    """For use with nodes or edges"""

    _queue: list = field(default_factory=lambda: [])  # type: ignore
    no_dup: bool = False

    def enqueue(self, item: Edge | Node) -> None:
        if self.no_dup:
            if item not in self._queue:
                self._queue.append(item)
        else:
            self._queue.append(item)

    def dequeue(self) -> Edge | Node:
        return self._queue.pop(0)

    def __bool__(self):
        return bool(self._queue)


class Graph:
    """Adjacency list representation of digraph
    Can only go forward along digraph (cannot traverse backwards)"""

    def __init__(self, nodes: list[Node] | None = None):

        self.src: None | Node = None

        if nodes:
            self.nodes: list[Node] = nodes  # list of items that need consideration
        else:
            self.nodes: list[Node] = []

        # initialise empty adjacency list
        self.adj_list: dict[Node, list[Edge]] = (
            {item: [] for item in nodes} if nodes else {}
        )

    def add_edge(self, current: Node, next: Node, value: int) -> None:
        """Add edge to the graph"""

        edge = Edge(next, -1 * value)

        # edges = self.adj_list[current]
        if current in self.adj_list.keys():
            self.adj_list[current].append(edge)
        else:
            self.adj_list[current] = [edge]

        dot.edge(
            f"{current.item_considered.label}{current.current_weight}",
            f"{next.item_considered.label}{next.current_weight}",
            f"{-1 * value}",
        )

    def neighbours(self, node: Node) -> list[Node]:
        """return the neighbours of a node"""
        edge: Edge
        if node in self.adj_list.keys():
            return [edge.next_node for edge in self.adj_list[node]]
        else:
            return []

    def edges_from(self, node: Node) -> list[Edge]:
        """return list of edges from a node"""
        return [edge for edge in self.adj_list[node]]

    def add_node(self, node: Node):
        """Adds node to graph with no edges"""
        self.adj_list[node] = []

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
                   for edge in self.adj_list[src_node]
               ]
            else False
        )

    def edge_weight(self, src: Node, dest: Node):
        """returns the weight of an edge - raises error if it does not exist"""
        if not self.is_edge(src, dest):
            raise EdgeDoesNotExistException

        else:
            return [edge.value for edge in filter(lambda x: x.next_node == dest, self.adj_list[src])][0]