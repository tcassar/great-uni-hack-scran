"""Solve the knapsack problem graphically"""

import src.engine.graph as graph


class Knapsack:
    """Methods to solve the knapsack problem
    Inputs:
        2d list of items: [[item_name, weight, value]...]
        Capacity
    """

    def __init__(self, cave: list[graph.Item], capacity: int):
        """
        Sets up knapsack

        cave is list of possible items in format [[item_name, weight, value]...]
        """
        self.cave: list[graph.Item] = cave
        self.capacity: int = capacity

    def build_graph(self):
        """Build the graph used to determine the best selection of items

        Algorithm:

        1) Generate (1, 0) - first item with no weight in knapsack
        2) Queue (1, 0)
        3) Generate sink node

        loop while there are items in the queue
            1) dequeue
            2) generate node and edge (i+1, w) - node if we don't take item i
            3) if w+w_i < capacity, generate node and edge (i+1, w+1_i) - node for taking item i
            4) if i+1 <= len(items), queue (i+1, w) and (i+1, w+w_i).
                else, we are in final layer thus create edge from nodes to sink node
        """

        queue = graph.Queue()

        # generate (1, 0)
        n0 = graph.Node(0, self.cave[0])
