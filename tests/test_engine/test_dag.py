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