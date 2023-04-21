"""
Bellman-Ford algorithm

Dijkstra breaks if there are negative weights.
Dijkstra is greedy, Bellman-Ford is dynamic.
"""


def bellman_ford(g, s, t):
    """
    arguments:
        g: directed graph, dict
            g[a][b] will be the cost of the edge a -> b
        s: starting node
        t: destination node

    returns:
        d: lenght of shortest path from s to t
    """
    # mem[i][v] will be the minimum cost of a path
    # from node v to node t having at most i edges
    mem = [{v: None for v in g} for _ in range(len(g))]
    mem[0] = {v: float("+inf") for v in g}
    mem[0][t] = 0

    for i in range(1, len(g)):
        for v in g:
            mem[i][v] = mem[i-1][v]
            for w in g[v]:
                cost = g[v][w] + mem[i-1][w]
                if cost < mem[i][v]:
                    mem[i][v] = cost

    return mem[len(g) - 1][s]


if __name__ == "__main__":
    g = {
        "a": {"u": 2, "b": 1},
        "b": {},
        "u": {"v": 3},
        "v": {"b": -6}
    }
    d = bellman_ford(g, "a", "b")
    assert d == -1

    g = {
        "a": {"c": 2, "d": 10},
        "b": {},
        "c": {"b": 1},
        "d": {"e": -20, "f": -5},
        "e": {"b": 10},
        "f": {"e": 6}
    }
    d = bellman_ford(g, "a", "b")
    assert d == 0

    print("all tests successful")
