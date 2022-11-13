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

        # enqueue src node
        q = graph.Queue([g.src], no_dup=True)

        # initialise maps to keep track of ...
        distance: dict[graph.Node, int] = {g.src: 0}  # distance from src
        origin: dict[graph.Node, graph.Node | None] = {g.src: None}  # node we came from

        # origin allows path to be rebuilt

        # BFS loop
        while q:
            current: graph.Node = q.dequeue()
            assert type(current) is graph.Node  # keep mypy happy
            for neighbour in g.neighbours(current):
                q.enqueue(neighbour)  # won't enqueue if already in queue

                # calculate distance to neighbour
                extra: int = g.edge_weight(current, neighbour)

                # if we haven't discovered neighbour yet initialise map with distance
                if neighbour not in distance.keys():
                    distance[neighbour] = extra + distance[current]
                    origin[neighbour] = current  # mark neighbour as having come from here
                else:
                    # if there is already an entry for distance, compute new overall distance and relax
                    # if necessary
                    if (new_dist := distance[current] + extra) < distance[neighbour]:
                        # shorted to get to neighbour via current thus update distance and origin
                        distance[neighbour] = new_dist
                        origin[neighbour] = current

        print(min(distance.values()))




