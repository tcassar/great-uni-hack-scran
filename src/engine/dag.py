"""DAG Shortest Path

Finds the shortest path through a weighted directed graph
where edge weights are in the set of integers

O(V+E)
"""

from src.engine import graph


class DAG:
    @staticmethod
    def shortest_path(g: graph.Graph) -> list[graph.Item]:
        """
        given a built knapsack problem graph, return a list of Items which
        maximise value while being under max weight
        """
