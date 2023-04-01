"""
Dijkstra's algorithm
https://www.wikiwand.com/en/Dijkstra%27s_algorithm
"""


from heap import Heap


class AdjEdge:
    def __init__(self, edge, nxt):
        self.edge = edge
        self.nxt = nxt


def dijkstra(g, s: int):
    """
    arguments:
        g: weighted directed graph, adjacency list
        s: key of starting node

    returns:
        distances: list
            distances[z] will be the length of the shortest path from s to z
    """
    n = len(g)  # number of nodes in the graph

    heap = Heap(max_size=n)
    heap.insert(key=s, value=0)

    distances = [None for _ in range(n)]
    distances[s] = 0

    while len(heap) > 0:
        closest_new_node_value, closest_new_node_key = heap.pop()
        distances[closest_new_node_key] = closest_new_node_value

        u = g[closest_new_node_key]
        while u:
            edge_length, neighbour_key = u.edge

            if distances[neighbour_key] is None:
                # we haven't yet found a shortest path to u
                dist = distances[closest_new_node_key] + edge_length
                if neighbour_key not in heap:
                    heap.insert(key=neighbour_key, value=dist)
                    heap[neighbour_key] = dist
                else:
                    heap_neighbour_value = heap[neighbour_key]
                    if heap_neighbour_value > dist:
                        heap[neighbour_key] = dist

            u = u.nxt

    return distances


if __name__ == "__main__":
    from enum import Enum

    class Rome(Enum):
        VERANO = 0
        PIAZZALE_ALDO_MORO = 1
        PORTA_MAGGIORE = 2
        TERMINI = 3
        TIBURTINA = 4
        LARGO_PRENESTE = 5
        VIALE_REGINA_ELENA = 6
        MENSA_DE_LOLLIS = 7
        MENSA_CASTRO_LAURENZIANO = 8

    graph = [
        # 0, VERANO
        AdjEdge((5, Rome.PIAZZALE_ALDO_MORO.value),
                AdjEdge((3, Rome.MENSA_DE_LOLLIS.value),
                        AdjEdge((4, Rome.MENSA_CASTRO_LAURENZIANO.value),
                                None))),

        # 1, PIAZZALE_ALDO_MORO
        AdjEdge((2, Rome.MENSA_DE_LOLLIS.value),
                None),

        # 2, PORTA_MAGGIORE
        AdjEdge((4, Rome.TERMINI.value),
                AdjEdge((4, Rome.VERANO.value),
                        None)),

        # 3, TERMINI
        AdjEdge((4, Rome.PORTA_MAGGIORE.value),
                None),

        # 4, TIBURTINA
        AdjEdge((4, Rome.VERANO.value),
                AdjEdge((6, Rome.LARGO_PRENESTE.value),
                        None)),

        # 5, LARGO_PRENESTE
        AdjEdge((4, Rome.PORTA_MAGGIORE.value),
                AdjEdge((10, Rome.VIALE_REGINA_ELENA.value),
                        AdjEdge((6, Rome.TIBURTINA.value),
                                None))),

        # 6, VIALE_REGINA_ELENA
        AdjEdge((1, Rome.MENSA_CASTRO_LAURENZIANO.value), None),

        # 7, MENSA_DE_LOLLIS
        AdjEdge((2, Rome.PIAZZALE_ALDO_MORO.value),
                None),

        # 8, MENSA_CASTRO_LAURENZIANO
        AdjEdge((1, Rome.VIALE_REGINA_ELENA.value),
                None),
    ]

    start = Rome.LARGO_PRENESTE.value
    distances = dijkstra(graph, start)

    assert distances[Rome.LARGO_PRENESTE.value] == 0
    assert None not in distances

    origin = Rome(start).name
    for i in range(len(distances)):
        destination = Rome(i).name
        print(f"distance from {origin} to {destination}: {distances[i]}")

    ##################################################
    print()

    graph = [
        # node v0
        # v0 -3-> v1
        # v0 -5-> v4
        AdjEdge((3, 1), AdjEdge((5, 4), None)),

        # node v1
        # v1 -2.5-> v2
        AdjEdge((2.5, 2), None),

        # node v2
        # v2 -1.5-> v3
        AdjEdge((1.5, 3), None),

        # node v3
        # no edges leave v3
        None,

        # node v4
        # v4 -1-> v3
        AdjEdge((1, 3), None)
    ]

    start = 0
    distances = dijkstra(graph, start)

    assert distances[start] == 0
    assert None not in distances

    for i in range(len(distances)):
        print(f"distance from v{start} to v{i}: {distances[i]}")

    ##################################################
    print()

    graph = [
        # (length, destination) edges leaving v0
        AdjEdge((1, 1), AdjEdge((4, 2), AdjEdge((2, 3), None))),

        # (length, destination) edges leaving v1
        AdjEdge((3, 4), AdjEdge((1, 2), None)),

        # (length, destination) edges leaving v2
        AdjEdge((1, 4), AdjEdge((2, 5), None)),

        # (length, destination) edges leaving v3
        AdjEdge((2, 2), AdjEdge((3, 5), None)),

        # no edges leaving v4
        None,

        # no edges leaving v5
        None
    ]

    start = 0
    distances = dijkstra(graph, start)

    assert distances[start] == 0
    assert distances[4] == 3
    assert distances[5] == 4

    for i in range(len(distances)):
        print(f"distance from v{start} to v{i}: {distances[i]}")

    ##################################################
    print()

    graph = [
        AdjEdge((1, 1), AdjEdge((10, 3), None)),
        AdjEdge((100, 4), AdjEdge((100, 2), None)),
        AdjEdge((1, 5), None),
        AdjEdge((10, 2), AdjEdge((10, 4), None)),
        AdjEdge((1, 5), None),
        None
    ]

    start = 0
    distances = dijkstra(graph, start)

    assert distances[start] == 0
    assert distances[5] == 21

    for i in range(len(distances)):
        print(f"distance from v{start} to v{i}: {distances[i]}")

    ##################################################
    print()

    print("all tests successful")
