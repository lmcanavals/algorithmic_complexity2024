from utils import graphs


def johnson(G):
    n = len(G)
    G.append([(n - 1, 0)])
    _, h = graphs.bellmanFord(G, n)
    if not h:
        return None, None  # negative cycle
    G.pop()
    G2 = [[] for _ in range(n)]
    for u in range(n):
        for v, w in G[u]:
            G2[u].append((v, w + h[u] - h[v]))

    paths = []
    costs = []
    for u in range(n):
        path, cost = graphs.dijkstra(G2, u)
        paths.append(path)
        costs.append(cost)

    return paths, costs


def solve():
    f = open('2.graph')
    labels = f.readline().split()
    lbl2idx = {lbl: idx for idx, lbl in enumerate(labels)}
    n = len(labels)
    G = [[] for _ in range(n)]
    for line in f:
        u, v, w = [int(v) if i == 2 else lbl2idx[v]
                   for i, v in enumerate(line.split())]
        G[u].append((v, w))

    paths, costs = johnson(G)
    if paths:
        print(paths)
        print(costs)
        graphs.show(G, labels=labels, directed=True, weighted=True,
                    path=paths[2]).view()


solve()
