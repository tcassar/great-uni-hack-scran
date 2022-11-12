from unittest import TestCase

from src.engine.knapsack import *


# TODO: write tests


class TestKnapsack(TestCase):
    def setUp(self):
        self.statue = graph.Item("statue", 4, 10)
        self.crystal = graph.Item("crystal", 2, 4)
        self.pen = graph.Item("pen", 3, 7)
        # create list from items
        self.items = [self.statue, self.crystal, self.pen]

        self.kp = Knapsack(self.items, 5)

    def test__new_nodes(self):
        Node, Item = graph.Node, graph.Item
        self.assertEqual(
            *self.kp._new_nodes(graph.Node(0, self.items[0])),
            [
                [
                    Node(0, Item(label="crystal", weight=2, value=4)),
                    Node(2, Item(label="crystal", weight=2, value=4)),
                ]
            ],
        )

    def test_build_graph(self):
        """build_graph
            Checks that graph built is the same as the one in the MIT lecture

            should have
            digraph G {

            rankdir=LR;

            A [label="(0, 0)"]
            B [label="(1, 0)"]
            C [label="(2, 0)"]
            E [label="(2, 2)"]
            F [label="(end, 2)"]
            G [label="(end, 3)"]
            H [label="(end, 0)"]
            I [label="(end, 4)"]
            J [label="(end, 5)"]
            K [label="(1, 4)"]
            L [label="(2, 4)"]

            Z [label="SINK"]

            F, G, H, I , J -> Z [label=0];

            A -> B -> C -> G -> H [label=" 0"];

            B -> E [label="-4", color="red"]
            E -> J [label="-7", color="red"]

            E -> F [label=0]

            A -> K [label=-10]
            K -> L  -> I[label=0]

        }

        """


        correct_dot = """// scran graph
digraph {
	statue0 [label="statue, 0"]
	"sink-1" [label="sink, -1"]
	crystal0 [label="crystal, 0"]
	crystal4 [label="crystal, 4"]
	statue0 -> crystal0 [label=0]
	statue0 -> crystal4 [label=-10]
	pen0 [label="pen, 0"]
	pen2 [label="pen, 2"]
	crystal0 -> pen0 [label=0]
	crystal0 -> pen2 [label=-4]
	pen4 [label="pen, 4"]
	crystal4 -> pen4 [label=0]
	final0 [label="final, 0"]
	final3 [label="final, 3"]
	pen0 -> final0 [label=0]
	pen0 -> final3 [label=-7]
	final2 [label="final, 2"]
	final5 [label="final, 5"]
	pen2 -> final2 [label=0]
	pen2 -> final5 [label=-7]
	final4 [label="final, 4"]
	pen4 -> final4 [label=0]
	final0 -> "sink-1" [label=0]
	final3 -> "sink-1" [label=0]
	final2 -> "sink-1" [label=0]
	final5 -> "sink-1" [label=0]
	final4 -> "sink-1" [label=0]
}
"""
        g: graph.Graph = self.kp.build_graph()
        print(graph.dot.source)
        self.assertEqual(correct_dot, graph.dot.source)