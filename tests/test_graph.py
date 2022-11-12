from src.engine.graph import *

from unittest import TestCase


class TestGraph(TestCase):
    def setUp(self) -> None:

        # create three items as in MIT lecture
        self.statue = Item("statue", 4, 10)
        self.crystal = Item("crystal", 2, 4)
        self.pen = Item("pen", 3, 7)

        # create list from items
        self.items = [self.statue, self.crystal, self.pen]

        # set knapsack capacity
        self.CAPACITY = 5

        # initialise graph
        self.graph = Graph(self.items, self.CAPACITY)

    def test_add_edge(self):
        """Checks that add_edge results in edge being added"""
        node = Node(0, self.statue)

        self.graph.add_edge(node, Node(4, self.crystal), node.item_considered.value)

        self.assertEqual(
            self.graph.adj_list[node.item_considered],
            [
                Edge(
                    next_node=Node(
                        current_weight=4,
                        item_considered=Item(label="crystal", weight=2, value=4),
                    ),
                    value=10,
                )
            ],
        )
