from unittest import TestCase
from src.engine.dag import *
from src.engine.knapsack import Knapsack

class TestDAG(TestCase):

    def test_shortest_path(self):

        with self.subTest('Check graph not built raises exception'):
            with self.assertRaises(GraphNotBuiltError):
                sp = DAG.shortest_path(graph.Graph())

        with self.subTest('Check that no error is raised when graph is built'):
            statue = graph.Item("statue", 4, 10)
            crystal = graph.Item("crystal", 2, 4)
            pen = graph.Item("pen", 3, 7)
            # create list from items
            items = [statue, crystal, pen]

            kp = Knapsack(items, 5)
            g = kp.build_graph()

            try:
                sp = DAG.shortest_path(g)
            except GraphNotBuiltError:
                self.fail('GraphNotBuiltError raised with built graph')

        print(sp)

    def test__build_items(self):

        Node, Item = graph.Node, graph.Item

        distance = {Node(0, Item(label='statue', weight=4, value=10)): 0, Node(0, Item(label='crystal', weight=2, value=4)): 0, Node(4, Item(label='crystal', weight=2, value=4)): -10, Node(0, Item(label='pen', weight=3, value=7)): 0, Node(2, Item(label='pen', weight=3, value=7)): -4, Node(4, Item(label='pen', weight=3, value=7)): -10, Node(0, Item(label='final', weight=0, value=0)): 0, Node(3, Item(label='final', weight=0, value=0)): -7, Node(2, Item(label='final', weight=0, value=0)): -4, Node(5, Item(label='final', weight=0, value=0)): -11, Node(4, Item(label='final', weight=0, value=0)): -10, Node(-1, Item(label='sink', weight=0, value=0)): -11}
        origin = {Node(0, Item(label='statue', weight=4, value=10)): None, Node(0, Item(label='crystal', weight=2, value=4)): Node(0, Item(label='statue', weight=4, value=10)), Node(4, Item(label='crystal', weight=2, value=4)): Node(0, Item(label='statue', weight=4, value=10)), Node(0, Item(label='pen', weight=3, value=7)): Node(0, Item(label='crystal', weight=2, value=4)), Node(2, Item(label='pen', weight=3, value=7)): Node(0, Item(label='crystal', weight=2, value=4)), Node(4, Item(label='pen', weight=3, value=7)): Node(4, Item(label='crystal', weight=2, value=4)), Node(0, Item(label='final', weight=0, value=0)): Node(0, Item(label='pen', weight=3, value=7)), Node(3, Item(label='final', weight=0, value=0)): Node(0, Item(label='pen', weight=3, value=7)), Node(2, Item(label='final', weight=0, value=0)): Node(2, Item(label='pen', weight=3, value=7)), Node(5, Item(label='final', weight=0, value=0)): Node(2, Item(label='pen', weight=3, value=7)), Node(4, Item(label='final', weight=0, value=0)): Node(4, Item(label='pen', weight=3, value=7)), Node(-1, Item(label='sink', weight=0, value=0)): Node(5, Item(label='final', weight=0, value=0))}
        DAG._build_items(origin, distance)