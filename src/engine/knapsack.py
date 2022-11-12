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
        self.cave_len = len(self.cave)

    def _next_nodes(self, current) -> tuple[list[graph.Node], int] | list:
        """Get a list of the nodes we can add to graph and the weights needed on their edge"""

        # check for last layer, if so return empty list
        if (next_index := self.cave.index(current.item_considered) + 1) > self.cave_len:
            return []

        if next_index < self.cave_len:
            next_item = self.cave[next_index]
        else:
            next_item = graph.Item('final', 0, 0)
            self.cave.append(next_item)

        nodes: list[tuple[graph.Node, int]] = [(graph.Node(current.current_weight, next_item), 0)]
        new_weight = current.current_weight + current.item_considered.weight
        if new_weight <= self.capacity:
            nodes.append((graph.Node(new_weight, next_item), current.item_considered.value))
        else:
            print('over capacity')

        return nodes




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

        # create starting node, sink node. add them to graph
        n0 = graph.Node(0, self.cave[0])
        sink = graph.Node(-1, graph.Item("sink", 0, 0))

        g = graph.Graph([n0.item_considered, sink.item_considered])
        q = graph.Queue([n0])

        while q:
            current = q.dequeue()
            if not (next_nodes := self._next_nodes(current)):
                # means we are in the last layer and thus connect current to sink
                g.add_edge(current, sink, 0)
                # dont queue
            else:
                for node, edge_weight in next_nodes:
                    g.add_node(node)
                    g.add_edge(current, node, edge_weight)
                    q.enqueue(node)
                    graph.dot.render(directory="./graphs/", filename=f"gen_graph.svg")

            graph.dot.render(directory="./graphs/", filename=f"gen_graph.svg")


