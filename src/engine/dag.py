"""DAG Shortest Path

Finds the shortest path through a weighted directed graph
where edge weights are in the set of integers

O(V+E)
"""

from src.engine import graph


class GraphNotBuiltError(Exception):
    """Graph has not been built - no source node found"""


class DAG:
    @staticmethod
    def shortest_path(g: graph.Graph) -> list[graph.Item]:
        """
        given a built knapsack problem graph, return a list of Items which
        maximise value while being under max weight

        modelled off BFS - keep track of distance from start for all nodes as well as which node we came from
        if we reach a node in a way that is shorter than from whence we came relax edges
        """

        # get first node of graph
        if g.src is None:
            raise GraphNotBuiltError


