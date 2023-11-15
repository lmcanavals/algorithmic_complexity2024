import math
from utils import graphs


def bellmanFord(G, s):
    n = len(G)
    g = [math.inf] * n
    path = [-1] * n
    g[s] = 0

    for _ in range(n - 1):
        for u in range(n):
            for v, w in G[u]:
                if g[u] + w < g[v]:
                    g[v] = g[u] + w
                    path[v] = u

    for u in range(n):
        for v, w in G[u]:
            if g[u] + w < g[v]:
                return None

    return path


def bftest():
    G = []
    with open("1.graph") as f:
        for line in f:
            if line.startswith('_'):
                G.append([])
                continue
            nums = list(map(int, line.split()))
            G.append([(nums[i], nums[i + 1]) for i in range(0, len(nums), 2)])

    path = bellmanFord(G, 0)
    if path:
        graphs.show(G, directed=True, weighted=True,
                    path=path, layout='circo').view()
    else:
        print("Negative cycle detected")


bftest()
