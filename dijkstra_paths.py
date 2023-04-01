"""
Dijkstra's algorithm
https://www.wikiwand.com/en/Dijkstra%27s_algorithm
"""


def dijkstra(g, s):
    """
    arguments:
        g: directed graph, dict
            g[a][b] will be the cost of the edge a -> b

        s: starting node

    returns:
        d: lenghts of shortest paths, dict
            d[z] will be the length of the shortest path from s to z

        p: shortest paths, lists of nodes
            p[z] will be a shortest path from s to z
    """
    d = {s: 0}
    p = {s: []}

    # set of visited nodes
    v = {s}

    # until we've visited all nodes
    while len(v) != len(g):
        # set of edges (start, neighbour) from visited starting nodes
        t = {
            (start, neighbour)
            for neighbour in (g.keys() - v)
            for start in v
            if neighbour in g[start]
        }

        # in _d[c] == (start, neighbour),
        # c will be the cost of s -> start -> neighbour
        _d = {
            d[start] + g[start][neighbour]: (start, neighbour)
            for start, neighbour in t
        }

        # mn = length shortest path exploring s -> start -> neighbour
        mn = min(_d.keys())
        start, neighbour = _d[mn]

        # visit this best neighbour
        # and remember this shortest path s -> neighbour
        d[neighbour] = mn
        p[neighbour] = p[start] + [neighbour]
        v.add(neighbour)

    return d, p


if __name__ == "__main__":
    g = {
        # v0 -3-> v1
        # v0 -5-> v4
        "v0": {"v1": 3, "v4": 5},

        # v1 -2.5-> v2
        "v1": {"v2": 2.5},

        # v2 -1.5-> v3
        "v2": {"v3": 1.5},

        # no edges leave v3
        "v3": {},

        # v4 -1-> v3
        "v4": {"v3": 1}
    }
    d, p = dijkstra(g, "v0")
    assert d == {
        "v0": 0,
        "v1": 3,
        "v2": 5.5,
        "v3": 6,
        "v4": 5
    }
    assert p == {
        "v0": [],
        "v1": ["v1"],
        "v2": ["v1", "v2"],
        "v3": ["v4", "v3"],
        "v4": ["v4"]
    }
    print(f"distances: {d}")
    print(f"shortest paths: {p}")

    ##################################################
    print()

    g = {
        "s": {"v1": 1, "v3": 10},
        "v1": {"v4": 100, "v2": 100},
        "v2": {"t": 1},
        "v3": {"v2": 10, "v4": 10},
        "v4": {"t": 1},
        "t": {}
    }
    d, p = dijkstra(g, "s")
    assert d["s"] == 0
    assert p["s"] == []

    cost = 0
    path = p["t"]
    last = "s"
    for node in path:
        cost += g[last][node]
        last = node
    assert cost == d["t"] == 21

    print(f"distances: {d}")
    print(f"shortest paths: {p}")

    ##################################################
    print()

    g = {
        "s": {"v1": 1, "v2": 4, "v3": 2},
        "v1": {"v4": 3, "v2": 1},
        "v2": {"v4": 1, "v5": 2},
        "v3": {"v2": 2, "v5": 3},
        "v4": {},
        "v5": {}
    }
    d, p = dijkstra(g, "s")
    assert d["v4"] == 3
    assert d["v5"] == 4
    print(f"distances: {d}")
    print(f"shortest paths: {p}")
