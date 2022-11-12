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

    def tearDown(self) -> None:
        print(f'rendering to {self.shortDescription()}.svg')
        dot.render(directory='./graphs', outfile=f'{self.shortDescription()}.svg')

    def test_add_edge(self):
        """
        add_edge
        Checks that add_edge results in edge being added"""
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
                    value=-10,
                )
            ],
        )

    def test_neighbours(self):
        """neighbours
        checks that neighbours list is returned properly"""

        # create 3 nodes
        n1 = Node(0, self.statue)
        n2 = Node(4, self.crystal)  # having taken statue
        n3 = Node(0, self.crystal)  # having skipped statue

        with self.subTest('no neighbours'):
            print(self.graph.adj_list)
            self.assertEqual(self.graph.neighbours(n1), [])

        with self.subTest('with neighbours'):

            # create edges
            self.graph.add_edge(n1, n2, 10)
            self.graph.add_edge(n1, n3, 0)

            self.assertEqual(self.graph.neighbours(n1), [n2, n3])

    def test_edges_from(self) -> None:
        """edges_from
        checks that we get edges from each node"""

        n1 = Node(0, self.statue)
        n2 = Node(4, self.crystal)  # having taken statue

        with self.subTest('no edges'):
            print(self.graph.adj_list)
            self.assertEqual(self.graph.edges_from(n1), [])

        with self.subTest('edge'):
            self.graph.add_edge(n1, n2, 10)
            self.assertEqual(self.graph.edges_from(n1), [Edge(n2, -10)])



